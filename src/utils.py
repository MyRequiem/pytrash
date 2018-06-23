#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# utils.py file is part of pytrash
#
# pytrash - implementation of the "trash" for Slackware linux
# Home page: https://github.com/MyRequiem/pytrash
#
# Copyright (c) 2018 Vladimir MyRequiem Astrakhan, Russia
# <mrvladislavovich@gmail.com>
# All rights reserved
# See LICENSE for details.


"""
Utils
"""


def get_full_path(file_path: str) -> str:
    """
    get full path
    """
    from os import path
    if file_path.endswith('/'):
        file_path = file_path[:-1]
    return path.abspath(path.expanduser(file_path))


def get_trash_path() -> list:
    """
    get trash path
    """
    trash = '~/.local/share/Trash'
    return [get_full_path('{0}/files'.format(trash)),
            get_full_path('{0}/info'.format(trash))]


def get_indent(width1: int, width2: int) -> str:
    """
    get space indent for format print
    """
    return ' ' * (width2 - width1)


def get_colors() -> dict:
    """
    colors
    """
    return {'red': '\x1b[0;31m',
            'lred': '\x1b[1;31m',
            'green': '\x1b[0;32m',
            'lgreen': '\x1b[1;32m',
            'yellow': '\x1b[0;33m',
            'lyellow': '\x1b[1;33m',
            'cyan': '\x1b[0;36m',
            'grey': '\x1b[38;5;247m',
            'reset': '\x1b[0m'}
