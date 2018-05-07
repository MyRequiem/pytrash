#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# main.py file is part of pytrash
#
# pytrash - implementation of the "trash" for Slackware linux
# Home page: https://github.com/MyRequiem/pytrash
#
# Copyright (c) 2018 Vladimir MyRequiem Astrakhan, Russia
# <mrvladislavovich@gmail.com>
# All rights reserved
# See LICENSE for details.


"""
main.py
"""

import sys
from os import path, rename

from .checktrashdirs import check_trash_dirs
from .helpmess import show_help_mess
from .utils import get_colors, get_full_path, get_indent, get_trash_path


class Main:
    """
    class Main
    """
    def __init__(self):
        self.args = sys.argv[1:]
        self.trash_path = get_trash_path()
        self.colors = get_colors()
        self.params = {
            '-h': self.show_help,
            '--help': self.show_help,
            '-d': self.move_to_trash,
            '--del': self.move_to_trash,
            '-f': self.restore,
            '--find': self.restore,
            '-r': self.restore,
            '--restore': self.restore,
            '-c': self.clear,
            '--clear': self.clear,
            '-s': self.get_trash_size,
            '--size': self.get_trash_size
        }

    def start(self) -> None:
        """
        parse arguments and launch of the relevant options
        """
        if not self.args or not self.args[0] in self.params:
            show_help_mess(True)
        else:
            if self.args[0] != '-h' and self.args[0] != '--help':
                check_trash_dirs()

            self.params[self.args[0]]()

    def show_help(self) -> None:
        """
        show help message
        """
        if len(self.args) == 1:
            show_help_mess()
        else:
            show_help_mess(True)

    def move_to_trash(self):
        """
        move file/dir to trash
        """
        if len(self.args) == 1:
            show_help_mess(True)

        from datetime import datetime
        for file_path in self.args[1:]:
            file_path = get_full_path(file_path)

            if not path.exists(file_path):
                print(('{0}File or directory{1} {2}{0} '
                       'not found{3}').format(self.colors['red'],
                                              self.colors['cyan'],
                                              file_path,
                                              self.colors['reset']))
                continue

            date = datetime.now().strftime("%d:%m:%y:%H:%M:%S.%f")
            new_name = '{0}/{1}__{2}'.format(path.dirname(file_path),
                                             date,
                                             file_path.split('/')[-1])
            rename(file_path, new_name)

            print('Move {0}{1}{2} to trash... '.format(self.colors['cyan'],
                                                       file_path,
                                                       self.colors['reset']),
                  end='')

            from shutil import move
            move(new_name, self.trash_path[0])
            print('{0}Ok{1}'.format(self.colors['lgreen'],
                                    self.colors['reset']))

            fobj = open('{0}/{1}'.format(self.trash_path[1],
                                         new_name.split('/')[-1]), 'w')
            fobj.write('{0}\n'.format(file_path))
            fobj.close()

    def restore(self):
        """
        restore file/dir from trash
        """
        len_args = len(self.args)
        if len_args > 2:
            show_help_mess(True)

        find = False
        if self.args[0] == '-f' or self.args[0] == '--find':
            if len_args == 1:
                show_help_mess(True)

            find = True

        from os import walk
        all_in_trash = list(walk(self.trash_path[0]))[0]
        list_dirs = all_in_trash[1]
        list_files = all_in_trash[2]
        list_files.extend(list_dirs)
        list_files.sort(reverse=True)

        if not list_files:
            print('{0}Trash is empty{1}'.format(self.colors['green'],
                                                self.colors['reset']))
            raise SystemExit

        if len_args > 1:
            tmp = []
            templ = self.args[1]
            for lfile in list_files:
                if lfile.find(templ) != -1:
                    tmp.append(lfile)
            if not tmp:
                print(('{0}Matches with template '
                       '{1}{2}{0} not found{3}').format(self.colors['red'],
                                                        self.colors['cyan'],
                                                        templ,
                                                        self.colors['reset']))
                raise SystemExit

            list_files = tmp

        num = 1
        for item in list_files:
            color = self.colors['cyan']
            end = ''
            if item in list_dirs:
                color = self.colors['yellow']
                end = '/'
            indent = get_indent(int(len(str(num))), 6)
            print(' {0}{1}{2}{3}{5}{4}'.format(num,
                                               indent,
                                               color,
                                               item,
                                               end,
                                               self.colors['reset']))
            num += 1

        if find:
            raise SystemExit

        while True:
            choice = input(('{0}Your choice for restore{1} '
                            '({2}q{1}uit){3}: ').format(self.colors['lyellow'],
                                                        self.colors['grey'],
                                                        self.colors['lred'],
                                                        self.colors['reset']))

            if choice == 'q':
                raise SystemExit

            if choice.isdigit():
                choice = int(choice)
                if 0 < choice <= len(list_files):
                    info_file = '{0}/{1}'.format(self.trash_path[1],
                                                 list_files[choice - 1])
                    if path.exists(info_file):
                        with open(info_file) as finfo:
                            for line in finfo:
                                path_for_restore = line.rstrip()
                                break

                        if not finfo.closed:
                            finfo.close()

                        path_for_restore = path.dirname(path_for_restore)
                        print(('Restore {0}{1}{4}\nto {2}{3}{4} '
                               '...').format(self.colors['cyan'],
                                             list_files[choice - 1],
                                             self.colors['yellow'],
                                             path_for_restore,
                                             self.colors['reset']),
                              end='')

                        if not path.exists(path_for_restore):
                            from os import makedirs
                            makedirs(path_for_restore)

                        rename('{0}/{1}'.format(self.trash_path[0],
                                                list_files[choice - 1]),
                               ('{0}/{1}-'
                                'restored').format(path_for_restore,
                                                   list_files[choice - 1]))
                        from os import remove
                        remove(info_file)
                        print(' {0}Ok{1}'.format(self.colors['lgreen'],
                                                 self.colors['reset']))
                        break
                    else:
                        print(('{0}Path to restore {1}{2}{0} '
                               'not found.{3}').format(self.colors['red'],
                                                       self.colors['cyan'],
                                                       list_files[choice - 1],
                                                       self.colors['reset']))

    def clear(self) -> None:
        """
        clear trash
        """
        if len(self.args) > 1:
            show_help_mess(True)

        choice = input(('{0}All files and directories from '
                        'trash will be deleted{1} '
                        '[yes/No]: ').format(self.colors['red'],
                                             self.colors['reset']))
        if choice != 'yes':
            print('Canceled')
        else:
            from shutil import rmtree
            rmtree(self.get_global_trash_path())
            check_trash_dirs()
            print('{0}Trash cleared{1}'.format(self.colors['green'],
                                               self.colors['reset']))

    def get_trash_size(self) -> None:
        """
        show trash size
        """
        if len(self.args) > 1:
            show_help_mess(True)

        import subprocess
        subprocess.call('du -sh {0}'.format(self.get_global_trash_path()),
                        shell=True)

    def get_global_trash_path(self) -> str:
        """
        return '~/.local/share/Trash'
        """
        return path.dirname(self.trash_path[0])
