def bash_completion():
    """
    Return a bash completion script for the borgmatic command. Produce this by introspecting
    borgmatic's command-line argument parsers.
    """
    import borgmatic
    import argparse
    import sys

    # Create a parser for the borgmatic command
    parser = borgmatic.create_parser()

    # Generate the completion script
    completion_script = f"""# Bash completion for borgmatic

_borgmatic_completion() {{
    local cur prev words cword
    _init_completion || return

    # Use the parser to get the list of commands and options
    local commands=$(compgen -W "$( {sys.argv[0]} --help | grep -oP '^[^ ]+' | tr '\\n' ' ' )" -- "$cur")
    COMPREPLY=( $(compgen -W "$commands" -- "$cur") )
}}

complete -F _borgmatic_completion borgmatic
"""

    return completion_script