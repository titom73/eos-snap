#!/usr/bin/python
# coding: utf-8 -*-

from typing import List
from pydantic import BaseModel


class SnapshotCommand(BaseModel):
    """
    SnapshotCommand Object for snapshot path
    """
    path_pre: str = None
    path_post: str = None

class TestDefinition(BaseModel):
    """
    TestDefinition Object for Test Definition

    Example:
    --------
    [
        {
            "name": "EOS Version",
            "command": "show version",
            "check_key": "version",
            "iterator": "$",
            "snapshot": {},
            "operator": "is_equal"
        },
        {
            "name": "BGP Session",
            "command": "show bgp evpn summary",
            "check_key": "peerState",
            "iterator": "vrfs.default.peers[* ]",
            "snapshot": {},
            "operator": "is_equal"
        }
    ]
    """
    name: str
    command: str
    snapshot: SnapshotCommand
    check_keys: List[str]
    iterator: str = 'key'
    status: bool = False
    checked: bool = False
    operator: str = 'is_equal'

class TestList(BaseModel):
    """
    TestList Object to list TestDefinition objects
    """
    __root__: List[TestDefinition]
    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, item):
        return self.__root__[item]

class ErrorMessage(BaseModel):
    """
    ErrorMessage: Error Message generated during snapshot comparison

    Example:
    --------
    {'key': '192.168.255.3', 'pre': 'Established', 'post': 'Down'}
    """
    key: str
    pre: str
    post: str

class TestResult(BaseModel):
    """
    TestResult Summary of Snapshot comparison

    Example:
    --------
    {'state': False, 'errors': [{'key': '192.168.255.3', 'pre': 'Established', 'post': 'Down'}]}
    """
    state: bool = False
    errors: List[ErrorMessage] = []
