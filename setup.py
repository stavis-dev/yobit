# -*- coding: utf-8 -*-
from os import path
from setuptools import setup, find_packages

# read the contents of your README file
try:
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except IOError:
    long_description = "Python Yobit Binding. Get pair and traders"


this_directory = path.abspath(path.dirname(__file__))
NAME = 'yobit'
about = {}
with open(path.join(this_directory, NAME, '__version__.py')) as f:
    exec(f.read(), about)

setup(
    name=NAME,
    version=about['__version__'],
    description="Python wrapper for yobit API v3",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="GNU",
    author="forked from NanoBjorn",
    author_email="",
    url="",
    packages=find_packages(exclude=('tests')),
    entry_points={'console_scripts': ['yobit=YoBit:main']},
    install_requires=['requests'],
    classifiers=["Programming Language :: Python",
                 "Programming Language :: Python :: 3",
                 ]
    )
