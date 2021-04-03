#!usr/bin/env/python3

import setuptools
from setuptools import setup

setup(
    name='scanzip',
    version='0.0.1',
    author='francois.nadeau.1',
    author_email='francois.nadeau.1@umontreal.ca',
    description="Module to help with zipfile compression, extraction, encoding and formatting",
    long_description="Module to help with zipfile compression, extraction, encoding and formatting",
    long_description_content_type='text/x-rst',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    url='https://github.com/FrancoisNadeau/scanzip.git',
    python_requires=">=3.6",
)
