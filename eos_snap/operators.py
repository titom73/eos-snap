#!/usr/bin/python
# coding: utf-8 -*-

import os
import json
from jsonpath_ng.ext import parse
from loguru import logger
from .resources.models import TestResult, ErrorMessage


class Operator():
    """
    Operator Implement supported eos-snap operators

    WIP

    TODO:
     - Use exception for error management
    """
    def __init__(self):
        pass

    @staticmethod
    def __is_equal_nested_dicts(data_pre, data_post, check_keys = None):
        """
        __is_equal_nested_dicts Helper to compare keys in nested dict

        Example:
        --------
        >>> print(data_pre)
        {
            "192.168.255.8": {
                ....,
                "peerState": "Active",
            },
            "192.168.255.9": {
                ....,
                "peerState": "Active",
            }
        }

        Args:
            data_pre (dict): dict of dict to compare with initial stage (pre)
            data_post (dict): dict of dict to compare with final stage (post)
            check_keys (List[str], optional): List of keys to compare

        Returns:
            TestResult: Result of comparison
        """
        if check_keys is None:
            check_keys = ['unset']
        result = TestResult()
        result.state = True
        for key_iteration, data in data_pre.items():
            if key_iteration not in data_post.keys():
                return TestResult(state=False, errors=[ErrorMessage(key=key_iteration, pre='Exists', post='Does not exist')])
            for check_key in check_keys:
                message = f'Comparison for {key_iteration} / {check_key}: before: <green>{data[check_key]}</> | after: <green>{data_post[key_iteration][check_key]}</>'
                if (
                    check_key in data
                    and data[check_key] != data_post[key_iteration][check_key]
                ):
                    result.state = False
                    error = ErrorMessage(key=key_iteration, pre=data[check_key], post=data_post[key_iteration][check_key])
                    result.errors.append(error)
                    message = f'Comparison for {key_iteration} / {check_key}: before: <red>{data[check_key]}</> | after: <red>{data_post[key_iteration][check_key]}</>'
                logger.opt(ansi=True).debug(message)
        return result

    @staticmethod
    def __is_equal_flat_dict(data_pre, data_post, check_keys = None):
        """
        __is_equal_flat_dict Helper to compare keys in flat dict

        Example:
        --------
        >>> print(data_pre)
        {
            "imageFormatVersion": "1.0",
            "uptime": 1893.46,
            "modelName": "vEOS-lab",
            "internalVersion": "4.27.0F-24305004.4270F",
            "memTotal": 2006636,
            "mfgName": "Arista",
            "serialNumber": "A3EFA4C9A67963BA8E57242ACE3CCE70",
            "systemMacAddress": "50:01:00:70:90:29",
            "bootupTimestamp": 1644422794.0,
            "memFree": 1100008,
            "version": "4.27.0F",
            "configMacAddress": "00:00:00:00:00:00",
            "isIntlVersion": false,
            "internalBuildId": "fed9e33b-669e-42ea-bee6-c7bf3cca1a73",
            "hardwareRevision": "",
            "hwMacAddress": "00:00:00:00:00:00",
            "architecture": "i686"
        }

        Args:
            data_pre (dict): flat dict to compare with initial stage (pre)
            data_post (dict): flat dict to compare with final stage (post)
            check_keys (List[str], optional): List of keys to compare

        Returns:
            TestResult: Result of comparison
        """
        if check_keys is None:
            check_keys = ['unset']
        result = TestResult()
        result.state = True
        for check_key in check_keys:
            if check_key in data_pre.keys() and check_key in data_post.keys():
                logger.debug(f'Comparison for {check_key}: {data_pre[check_key]} | {data_post[check_key]}')
                if data_pre[check_key] != data_post[check_key]:
                    result.state = False
                    error = ErrorMessage(key=check_key, pre=data_pre[check_key], post=data_post[check_key])
                    result.errors.append(error)
        return result

    @staticmethod
    def is_equal(data_pre, data_post, keys: list):
        """
        is_equal Generic entrypoint for is_equal operator

        WIP

        Args:
            keys (list): [description]

        Returns:
            [type]: [description]
        """
        # Load operator for nested dict
        if any(isinstance(d, dict) for d in data_pre.values()):
            return Operator.__is_equal_nested_dicts(data_post=data_post, data_pre=data_pre, check_keys=keys)
        if isinstance(data_pre, dict):
            return Operator.__is_equal_flat_dict(data_post=data_post, data_pre=data_pre, check_keys=keys)
        logger.critical('Data structure not yet supported')
        return TestResult(state=False, errors=[])