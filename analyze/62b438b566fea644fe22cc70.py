def bash_completion():
    """
    Restituisci uno script bash di completamento per il comando "borgmatic". Genera questo script analizzando i parser degli argomenti della riga di comando di "borgmatic".
    """
    import subprocess

    # Get the list of commands and options from borgmatic
    try:
        output = subprocess.check_output(['borgmatic', '--help'], universal_newlines=True)
    except subprocess.CalledProcessError:
        return ""

    # Parse the output to extract commands and options
    commands = []
    options = []
    lines = output.splitlines()
    is_command_section = False
    is_option_section = False

    for line in lines:
        if line.startswith('Commands:'):
            is_command_section = True
            is_option_section = False
            continue
        elif line.startswith('Options:'):
            is_command_section = False
            is_option_section = True
            continue

        if is_command_section and line.strip():
            commands.append(line.split()[0])  # Get the command name
        elif is_option_section and line.strip():
            options.append(line.split()[0])  # Get the option name

    # Generate the bash completion script
    completion_script = """
# Bash completion for borgmatic
_borgmatic_completion() {
    local commands
    local options

    commands=(
        {}
    )

    options=(
        {}
    )

    COMPREPLY=()
    local cur="${COMP_WORDS[COMP_CWORD]}"
    local prev="${COMP_WORDS[COMP_CWORD-1]}"

    if [[ ${COMP_CWORD} -eq 1 ]]; then
        COMPREPLY=( $(compgen -W "${commands[*]}" -- "$cur") )
    else
        COMPREPLY=( $(compgen -W "${options[*]}" -- "$cur") )
    fi
}

complete -F _borgmatic_completion borgmatic
""".format(' '.join(commands), ' '.join(options))

    return completion_script