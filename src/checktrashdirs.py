#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# checktrashdirs.py file is part of pytrash
#
# pytrash - implementation of the "trash" for Slackware linux
# Home page: https://github.com/MyRequiem/pytrash
#
# Copyright (c) 2018 Vladimir MyRequiem Astrakhan, Russia
# <mrvladislavovich@gmail.com>
# All rights reserved
# See LICENSE for details.


"""
check if a trash dirs exists and create its if needed
"""

from os import makedirs, path

from .utils import get_trash_path


def check_trash_dirs():
    """
    check if a trash dirs exists and create its if needed
    """
    for tpath in get_trash_path():
        if not path.exists(tpath):
            makedirs(tpath)
