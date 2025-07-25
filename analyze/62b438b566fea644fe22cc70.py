import argparse
import sys

def bash_completion():
    """
    Return a bash completion script for the borgmatic command. Produce this by introspecting
    borgmatic's command-line argument parsers.
    """
    parser = argparse.ArgumentParser(description='Generate bash completion script for borgmatic.')
    parser.add_argument('--command', help='The borgmatic command to generate completion for.', required=True)
    parser.add_argument('--output', help='Output file to write the completion script to.', default=sys.stdout)

    args = parser.parse_args()

    completion_script = f"""
    #!/bin/bash
    _borgmatic_completion() {{
        local cur prev opts
        COMPREPLY=()
        cur="${{COMP_WORDS[COMP_CWORD]}}"
        prev="${{COMP_WORDS[COMP_CWORD-1]}}"
        opts="$(borgmatic --help | grep -oP '^\\s+\\K[^\\s]+')"

        if [[ ${{cur}} == -* ]]; then
            COMPREPLY=( $(compgen -W "${{opts}}" -- ${{cur}}) )
        else
            COMPREPLY=( $(compgen -f -- ${{cur}}) )
        fi
    }}
    complete -F _borgmatic_completion {args.command}
    """

    if args.output == sys.stdout:
        print(completion_script)
    else:
        with open(args.output, 'w') as f:
            f.write(completion_script)

    return completion_script