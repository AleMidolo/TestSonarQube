import argparse
import sys

def bash_completion():
    """
    Return a bash completion script for the borgmatic command. Produce this by introspecting
    borgmatic's command-line argument parsers.
    """
    parser = argparse.ArgumentParser(description='Borgmatic command-line tool.')
    parser.add_argument('--version', action='store_true', help='Show the version and exit.')
    parser.add_argument('--config', help='Path to the configuration file.')
    parser.add_argument('--verbosity', type=int, choices=[0, 1, 2], help='Set verbosity level (0, 1, or 2).')
    parser.add_argument('--list', action='store_true', help='List all available commands.')
    parser.add_argument('--help', action='store_true', help='Show this help message and exit.')

    # Generate bash completion script
    script = """
_borgmatic_completion() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="--version --config --verbosity --list --help"

    if [[ ${cur} == -* ]]; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi
}

complete -F _borgmatic_completion borgmatic
"""
    return script

if __name__ == "__main__":
    print(bash_completion())