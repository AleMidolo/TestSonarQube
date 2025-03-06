import argparse
import sys

def bash_completion():
    """
    Return a bash completion script for the borgmatic command. Produce this by introspecting
    borgmatic's command-line argument parsers.
    """
    parser = argparse.ArgumentParser(description='Generate bash completion script for borgmatic.')
    parser.add_argument('--command', help='The command to generate completion for', default='borgmatic')
    parser.add_argument('--output', help='Output file for the completion script', default='/etc/bash_completion.d/borgmatic')

    args = parser.parse_args()

    completion_script = f"""
# bash completion for {args.command}
_{args.command}() {{
    local cur prev opts
    COMPREPLY=()
    cur="${{COMP_WORDS[COMP_CWORD]}}"
    prev="${{COMP_WORDS[COMP_CWORD-1]}}"
    opts="$( {args.command} --help | grep -oP '^\\s+\\K[^\\s]+' )"

    if [[ ${{cur}} == -* ]]; then
        COMPREPLY=( $(compgen -W "${{opts}}" -- ${{cur}}) )
    else
        COMPREPLY=( $(compgen -f ${{cur}}) )
    fi
}}

complete -F _{args.command} {args.command}
"""

    with open(args.output, 'w') as f:
        f.write(completion_script)

    print(f"Bash completion script for {args.command} has been written to {args.output}")

if __name__ == "__main__":
    bash_completion()