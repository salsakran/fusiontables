#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import fusiontables

setup(
    name='fusiontables',
    version="0.0.1",
    description="Fusion tables API",
    author="someone at google",
    author_email="someone@google.com",
    url='http://code.google.com/p/fusion-tables-client-python/',
    license='Apache 2.0',
    platforms=["any"],
    packages=find_packages(exclude=['ez_setup']),
    install_requires=[
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
    ],
    long_description=codecs.open('README', "r", "utf-8").read(),
)
