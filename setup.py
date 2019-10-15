#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:33:49 2019

@author: quentinpeter
"""


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="applaunchservices",
    version="0.1.5",
    author="Quentin Peter",
    author_email="qpeter@bluewin.ch",
    description="Simple package for registering an app with apple Launch Services to handle UTI and URL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/impact27/applaunchservices",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
)
