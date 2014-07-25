#!/usr/bin/env python
# coding=utf-8

from distutils.core import setup

setup(
    name = "gam",
    version = "0.1",
    description = "simple single message base of udp",
    long_description = open('README.md').read()
    author = "cnsworder",
    author_email = "cnsworder@gmail.com",
    packages = ["gam"],
    install_requires = ['pyyaml'],
)
