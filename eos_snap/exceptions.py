#!/usr/bin/python
# coding: utf-8 -*-

from loguru import logger

class Error(Exception):
    """Base class for other exceptions"""
    pass

class FolderNotFound(Error):
    """Raised when destination folder is not found"""
    def __init__(self, folder):
        self.message = f'{folder} is not found!'
        logger.error(self.message)
