#!/usr/bin/python
# coding: utf-8 -*-

from setuptools import setup
import eos_snap

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="eos_snap",
    version="{}".format(eos_snap.__version__),
    python_requires=">=3.8",
    packages=['eos_snap'],
    scripts=["bin/tester.py"],
    install_requires=required,
    include_package_data=True,
    url="https://github.com/titom73/arista-downloader",
    license="APACHE",
    author="{}".format(eos_snap.__author__),
    author_email="{}".format(eos_snap.__email__),
    description=long_description,
)