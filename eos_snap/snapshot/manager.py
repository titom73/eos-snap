#!/usr/bin/python
# coding: utf-8 -*-

import os
import json
from dataclasses import dataclass
from loguru import logger
from ..test import TestCollection
from ..resources.exceptions import *


class SnapshotManager():
    """
    SnapshotManager Helper to manage snapshot content and paths
    """
    def __init__(self, root_path: str = 'tests/'):
        self.root_path = root_path

    def _generate_dir(self, snapshot_path):
        """
        _generate_dir Create snapshot directory if not already existing

        Args:
            snapshot_path (str): Path to check and create if required

        Returns:
            bool: True if exist or successfully created, False in other cases
        """
        if os.path.isdir(snapshot_path) is False:
            try:
                logger.debug('  - Generate folder {} to save snapshot', snapshot_path)
                os.makedirs(snapshot_path)
            except Error as exc:
                logger.critical('Can\'t create folder {} - {}', snapshot_path, exc)
            return True
        return False

    def destination_folder(self, host: str, prefix: str):
        """
        destination_folder generate folder path for a HOST and a STAGE

        Args:
            host (str): Host to consider
            prefix (str): Snapshot stage to consider

        Returns:
            str: relative path for snapshot
        """
        return f'{self.root_path}/{host}/{prefix}'

    def save_snapshot(self, host:str, prefix: str, test_data):
        """
        save_snapshot Save command output in dedicated snapshot file ordered by host and stage

        Args:
            host (str): host from where content comes
            prefix (str): Stage of the snapshot
            test_data (TestDefinition): Test object to read command

        Returns:
            str: Filepath for the command snapshot
        """
        self._generate_dir(self.destination_folder(host=host, prefix=prefix))
        filepath = (
            f'{self.destination_folder(host=host, prefix=prefix)}/'
            + test_data['command'].replace(' ', '_')
            + '.json'
        )

        logger.info('Save command "{}" to {} for host {}', test_data['command'], filepath, host)
        with open(filepath, "w") as json_file:
            json.dump(test_data['result'], json_file, indent=4)
        return filepath

    def get_snapshot_path(self, test: dict, host:str, prefix: str,):
        """
        get_snapshot_path Find snapshot path for a command, host, prefix

        Args:
            test (TestDefinition): Test to read command
            host (str): Host to consider
            prefix (str): Stage to consider

        Returns:
            str: Filepath with snapshot content
        """
        filepath = (
            f'{self.destination_folder(host=host, prefix=prefix)}/'
            + test.command.replace(' ', '_')
            + '.json'
        )
        return filepath if os.path.isfile(filepath) else None

