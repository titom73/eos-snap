#!/usr/bin/python
# coding: utf-8 -*-

from importlib.resources import path
import sys
from jsonpath_ng.ext import parse
import json
from loguru import logger
from eos_snap import *
from eos_snap.show_bgp_summary import EOS_DATA
from eos_snap.devices import DeviceEos
from eos_snap.test import TestCollection

DEVICES = ['veos01']

TEST_CASES = [{
        'name': 'Demo test1',
        'command': 'show interfaces description',
        'path': 'interfaceDescriptions[*]',
        'check_key': 'interfaceStatus',
        'iterator': 'description',
        'snapshot': {}
    },
    {
        'name': 'Demo test2',
        'command': 'show bgp evpn summary',
        'path': 'result[*].vrfs.default.peers[*]',
        'check_key': 'peerState',
        'iterator': 'description',
        'snapshot': {}
    }
]


def read_json():
    jsonpath_expr = parse('result[*].vrfs.default.peers[*]..peerState')
    data_set = json.loads(EOS_DATA)
    return [{str(match.full_path): match.value} for match in jsonpath_expr.find(data_set)]

def example():
    jsonpath_expr = parse('foo[*].baz')
    return [match.value for match in jsonpath_expr.find({'foo': [{'baz': 1}, {'baz': 2}]})]


if __name__ == '__main__':
    logger.remove()
    logger.add(sys.stderr, level='DEBUG', colorize=True)

    logger.warning('Test JSON PATH')
    # logger.info('Run web example')
    # logger.info(str(example()))

    logger.info('Found following entries for peerState')
    logger.info(str(read_json()))


    logger.warning('** TestCollection')
    my_collection = TestCollection()
    my_collection.add_json_test(TEST_CASES)
    for test in my_collection.collection:
        logger.info(' - {}', test.name)
    my_collection.update_test(new_name='test-test-test')
    for test in my_collection.collection:
        logger.info(' - {}', test.name)

    logger.warning('** Test DeviceEos')
    eos = DeviceEos(hostname='veos01', test_cases=TEST_CASES)
    eos.generate_snapshot(prefix='pre')

    for test_case in eos.test_cases.collection:
        logger.info('Test {} has pre snapshot saved under {}', test_case.name, test_case.snapshot.path_pre)

    logger.critical('Closing test program')
    sys.exit(0)