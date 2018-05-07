---
# PyTrash
>###### PyTrash is a CLI implementation of the "trash" for Slackware linux
>###### This program is available on [SlackBuilds.org][1]
---
##### Main features:
* remove to trash
* search in trash
* restore from trash
* clear trash
* show trash size

##### Requirements:
* Python 3.0+ (available on SlackBuilds.org)

##### Build and install:
1. `~# wget https://github.com/MyRequiem/pytrash/archive/1.1.0/pytrash-1.1.0.tar.gz`
2. `~# tar -xvzf pytrash-1.1.0.tar.gz`
3. `~# cd pytrash-1.1.0/slackbuild`
4. `~# ./pytrash.SlackBuild`
5. `~# upgradepkg --install-new --reinstall /tmp/pytrash-1.1.0-*.t?z`

##### Usage:
##### -h, --help

Print this help message and exit

##### -d, --del path/to/file_or_dir [path/to/file_or_dir ...]

Move files/dirs to trash (~/.local/share/Trash/)

##### -f, --find pattern

Search for files and directories in the trash

##### -r, --restore [pattern]

Print list of files/dirs on trash with the possibility of their recovery.
If the pattern is specified, then only matches with this pattern are displayed.

##### -c, --clear

Clear trash

##### -s, --size

Show the size of the trash

[1]: https://slackbuilds.org/repository/14.2/system/pytrash/
