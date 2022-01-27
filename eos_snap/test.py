#!/usr/bin/python
# coding: utf-8 -*-

from cgi import test
import json
from typing import List
from .pydantic import TestDefinition
from pydantic import parse_obj_as
from .exceptions import *


class TestCollection():
    def __init__(self, json_tests: str = None):
        self._collection: list = []
        if json_tests is not None:
            self.add_json_test(tests = json_tests)

    def add_json_test(self, tests):
        for test in tests:
            self._collection.append(TestDefinition.parse_raw(json.dumps(test)))

    @property
    def collection(self):
        return self._collection

    def update_test(self, new_name: str):
        for test in self._collection:
            test.name = new_name
