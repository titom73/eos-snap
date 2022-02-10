#!/usr/bin/python
# coding: utf-8 -*-

import os
import json
from dataclasses import dataclass
from loguru import logger
from typing import Dict
import pyeapi
from .test import TestCollection
from .snapshot.manager import SnapshotManager
from .resources.exceptions import *


class DeviceEos():
    """
    DeviceEos EOS device Test representation

    Help to manage data for EOS devices:
    - Load data from snapshot
    - Get data from devices
    """
    def __init__(self,hostname: str, test_cases: dict, snapshot_root: str = 'tests'):
        self.hostname = hostname
        self.test_cases = TestCollection(json_tests=test_cases)
        # TODO: Add support for offline mode to be able to load snapshot with no access to devices
        self.connector = EosConnector(device_name=hostname)
        self.snapshot = SnapshotManager(root_path=snapshot_root)

    def generate_snapshot(self, prefix: str = 'pre'):
        """
        generate_snapshot  Get snapshot path from command defined in configuration file

        Args:
            prefix (str, optional): Which stage of the run. Defaults to 'pre'.
        """
        eos_commands = [test_case.command for test_case in self.test_cases.collection]
        eos_data = self.connector.collect_commands(commands=eos_commands)
        for test_case in self.test_cases.collection:
            eos_result = next(eos_result for eos_result in eos_data if eos_result['command'] == test_case.command)
            if prefix == 'pre':
                test_case.snapshot.path_pre = self.snapshot.save_snapshot(
                    host=self.hostname,
                    prefix=prefix,
                    test_data=eos_result
                )
            elif prefix == 'post':
                test_case.snapshot.path_post = self.snapshot.save_snapshot(
                    host=self.hostname,
                    prefix=prefix,
                    test_data=eos_result
                )

    def load_saved_snapshot(self, prefix: str = 'pre'):
        """
        load_saved_snapshot Get snapshot path from filesystem

        Used when you run comparison and your snapshot have been saved in a previous script

        Args:
            prefix (str, optional): Which stage to load. Defaults to 'pre'.
        """
        for test_case in self.test_cases.collection:
            if prefix == "pre":
                test_case.snapshot.path_pre = self.snapshot.get_snapshot_path(
                    host=self.hostname,
                    prefix=prefix,
                    test=test_case
                )
            elif prefix == "post":
                test_case.snapshot.path_post = self.snapshot.get_snapshot_path(
                    host=self.hostname,
                    prefix=prefix,
                    test=test_case
                )


class EosConnector():
    """
    EosConnector Helper to get data from EOS devices
    """
    def __init__(self, device_name: str):
        self.node = pyeapi.connect_to(device_name)
        self._get_facts()

    def _get_facts(self):
        """
        _get_facts Get output of show version to test connectivity
        """
        self.facts = self.node.enable('show version')[0]['result']

    def collect_commands(self, commands: list):
        """
        collect_commands Execute an eAPI call to get data for a list of commands

        Execute a call for a list of commands

        Args:
            commands (list): List of EOS command to retrieve.

        Returns:
            dict: data returns by EOS
        """
        return self.node.enable(commands)