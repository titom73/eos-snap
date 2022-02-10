#!/usr/bin/python
# coding: utf-8 -*-

import os
import json
from jsonpath_ng.ext import parse
from loguru import logger
from ..resources.models import TestResult
from ..operators import Operator


class SnapshotTester():
    """
    SnapshotTester Run test comparison between 2 snapshots
    """
    def __init__(self, path_pre: any, path_post: any, iterator: str = None):
        """
        __init__ Constructor

        Load data from paths and execute testing

        Args:
            path_pre (str): Path to PRE snapshot file
            path_post (any): [description]
            iterator (str, optional): JSON path query to iterate over data. Defaults to None.
        """
        self.pre = self._load_data(path=path_pre)
        self.post = self._load_data(path=path_post)
        self.iterator = iterator

    def _load_data(self, path):
        """
        _load_data Helper to load data from file

        Args:
            path (str): Path to file

        Returns:
            Any: JSON content from the file
        """
        if os.path.isfile(path):
            with open(path) as json_file:
                return json.load(json_file)
        return '{}'

    def _clean_structure(self, data):
        """
        _clean_structure Remove unnecessary list structure generated by the JSONPath query

        Args:
            data (List): List of JSON data

        Returns:
            dict: JSON data without List header
        """
        if isinstance(data, list) and len(data) == 1:
            data = data[0]
        return data

    def _json_extract(self, iterator: str, stage: str = 'pre' ):
        """
        _json_extract Extract JSON data from JSON path query

        Uses test iterator to get relevant information to use in comparison

        Args:
            iterator (str): JSON path syntax to use to extract data
            stage (str, optional): Which stage to use to extract data. Defaults to 'pre'.

        Returns:
            JSON: JSON data catch by JSON path query
        """
        logger.debug(f'JSON iterator is set to: {iterator} for {stage}')
        jsonpath_expr = parse(iterator)
        if stage == 'pre':
            return self._clean_structure([match.value for match in jsonpath_expr.find(self.pre)])
        else:
            return self._clean_structure([match.value for match in jsonpath_expr.find(self.post)])

    def is_equal(self, keys: list):
        """
        is_equal Generic entrypoint for is_equal operator

        WIP

        Args:
            keys (list): [description]

        Returns:
            [type]: [description]
        """
        data_pre = self._json_extract(stage='pre', iterator=self.iterator)
        data_post = self._json_extract(stage='post', iterator=self.iterator)
        # Load operator for nested dict
        if any(isinstance(d, dict) for d in data_pre.values()):
            return Operator.is_equal_nested_dicts(data_post=data_post, data_pre=data_pre, check_keys=keys)
        if isinstance(data_pre, dict):
            return Operator.is_equal_flat_dict(data_post=data_post, data_pre=data_pre, check_keys=keys)
        logger.critical('Data structure not yet supported')
        return TestResult(state=False, errors=[])
