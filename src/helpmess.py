#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# helpmess.py file is part of pytrash
#
# pytrash - implementation of the "trash" for Slackware linux
# Home page: https://github.com/MyRequiem/pytrash
#
# Copyright (c) 2018 Vladimir MyRequiem Astrakhan, Russia
# <mrvladislavovich@gmail.com>
# All rights reserved
# See LICENSE for details.


"""
Help messages and usage
"""

from .utils import get_colors


def show_help_mess(error: bool = False) -> None:
    """Usage: pytrash <param> [param[, param ...]]

    {0}-h, --help{1}
        Print this help message and exit.

    {0}-d, --del <path> [path[ path ...]]{1}
        Move files/dirs to trash (~/.local/share/Trash/).

    {0}-f, --find <pattern>{1}
        Search for files and directories in the trash.

    {0}-r, --restore [pattern]{1}
        Print list of files/dirs on trash with the possibility
        of their recovery. If the pattern is specified, then
        only matches with this pattern are displayed.

    {0}-c, --clear{1}
        Clear trash.

    {0}-s, --size{1}
        Show the size of the trash.
"""

    colors = get_colors()
    if error:
        print(('{0}Wrong parameters.{1} '
               '\'pytrash --help\'{2} for help').format(colors['red'],
                                                        colors['cyan'],
                                                        colors['reset']))
        raise SystemExit

    # show usage
    print(str(show_help_mess.__doc__).format(colors['cyan'], colors['reset']))
