import argparse
import sys

def bash_completion():
    """
    Return a bash completion script for the borgmatic command. Produce this by introspecting
    borgmatic's command-line argument parsers.
    """
    parser = argparse.ArgumentParser(description='Borgmatic command-line interface.')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add subcommands and their arguments
    init_parser = subparsers.add_parser('init', help='Initialize a new borgmatic repository')
    init_parser.add_argument('--encryption', choices=['repokey', 'keyfile'], help='Encryption type')
    init_parser.add_argument('--append-only', action='store_true', help='Enable append-only mode')

    create_parser = subparsers.add_parser('create', help='Create a new backup')
    create_parser.add_argument('--exclude', action='append', help='Exclude patterns')
    create_parser.add_argument('--compression', choices=['lz4', 'zstd'], help='Compression algorithm')

    prune_parser = subparsers.add_parser('prune', help='Prune old backups')
    prune_parser.add_argument('--keep-daily', type=int, help='Number of daily backups to keep')
    prune_parser.add_argument('--keep-weekly', type=int, help='Number of weekly backups to keep')

    check_parser = subparsers.add_parser('check', help='Check the integrity of backups')
    check_parser.add_argument('--repair', action='store_true', help='Attempt to repair any issues')

    # Generate bash completion script
    script = """
_borgmatic_completion() {
    local cur prev commands
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    commands="init create prune check"

    if [[ ${cur} == -* ]]; then
        local opts=""
        case "${prev}" in
            init)
                opts="--encryption --append-only"
                ;;
            create)
                opts="--exclude --compression"
                ;;
            prune)
                opts="--keep-daily --keep-weekly"
                ;;
            check)
                opts="--repair"
                ;;
            *)
                ;;
        esac
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi

    if [[ ${prev} == borgmatic ]]; then
        COMPREPLY=( $(compgen -W "${commands}" -- ${cur}) )
        return 0
    fi
}

complete -F _borgmatic_completion borgmatic
"""
    return script