#!/usr/bin/python
# coding: utf-8 -*-

import os
import json
from dataclasses import dataclass
from loguru import logger
from typing import Dict
import pyeapi
from .test import TestCollection
from .exceptions import *


class DeviceEos():
    def __init__(self,hostname: str, test_cases: dict, snapshot_root: str = 'tests'):
        self.hostname = hostname
        self.test_cases = TestCollection(json_tests=test_cases)
        self.connector = EosConnector(device_name=hostname)
        self.snapshot = SnapshotManager(root_path=snapshot_root)

    def generate_snapshot(self, prefix: str = 'pre'):
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

class SnapshotManager():
    def __init__(self, root_path: str = 'tests/'):
        self.root_path = root_path

    def _generate_dir(self, snapshot_path):
        if os.path.isdir(snapshot_path) is False:
            try:
                logger.debug('  - Generate folder {} to save snapshot', snapshot_path)
                os.makedirs(snapshot_path)
            except Error as exc:
                logger.critical('Can\'t create folder {} - {}', snapshot_path, exc)
            return True
        return False

    def save_snapshot(self, host:str, prefix: str, test_data):
        destination_folder = self.root_path + '/' + host + '/' + prefix
        self._generate_dir(destination_folder)
        filepath = destination_folder + '/' + test_data['command'].replace(' ', '_') + '.json'
        logger.info('Save command "{}" to {} for host {}', test_data['command'], filepath, host)
        with open(filepath, "w") as json_file:
            json.dump(test_data['result'], json_file, indent=4)
        return filepath

class EosConnector():
    def __init__(self, device_name: str):
        self.node = pyeapi.connect_to(device_name)
        self._get_facts()

    def _get_facts(self):
        self.facts = self.node.enable('show version')[0]['result']

    def collect_commands(self, commands: list):
        return self.node.enable(commands)