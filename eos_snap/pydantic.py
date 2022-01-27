#!/usr/bin/python
# coding: utf-8 -*-

from typing import List
from pydantic import BaseModel


class SnapshotCommand(BaseModel):
    path_pre: str = None
    path_post: str = None

class TestDefinition(BaseModel):
    name: str
    command: str
    snapshot: SnapshotCommand
    check_key: str
    iterator: str = 'key'
    status: bool = False
    checked: bool = False

class TestList(BaseModel):
    __root__: List[TestDefinition]
    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, item):
        return self.__root__[item]
