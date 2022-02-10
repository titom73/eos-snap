#!/usr/bin/python
# coding: utf-8 -*-

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from loguru import logger
import yaml

__author__ = '@titom73'
__email__ = 'tom@inetsix.net'
__date__ = '2022-02-10'
__version__ = '0.2.0'


def load_configuration(yaml_path: str):
    """
    load_configuration Configuration loader from YAML file

    Args:
        yaml_path (str): Path of the YAML file to load as configuration

    Returns:
        dict: Dictionary of configuration
    """
    with open(yaml_path, "r") as stream:
        try:
            configuration = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logger.error(exc)
    return configuration['eos_snapshot']