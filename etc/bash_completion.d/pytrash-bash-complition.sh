#!/bin/bash

_pytrash() {
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"

    subcommands_main="--help --del --find --restore --clear --size"

    if [[ ${COMP_CWORD} == 1 ]] ; then
        COMPREPLY=($(compgen -W "${subcommands_main}" -- "${cur}"))
        return 0
    fi
}

complete -F _pytrash pytrash
