def bash_completion():
    """
    Restituisci uno script bash di completamento per il comando "borgmatic". Genera questo script analizzando i parser degli argomenti della riga di comando di "borgmatic".
    """
    import subprocess

    # Get the list of commands and options from borgmatic
    try:
        output = subprocess.check_output(['borgmatic', '--help'], universal_newlines=True)
    except subprocess.CalledProcessError as e:
        return f"Error while fetching help: {e}"

    # Parse the output to extract commands and options
    commands = []
    options = []
    lines = output.splitlines()

    for line in lines:
        if line.startswith('  '):  # Indentation indicates options
            options.append(line.strip())
        elif line and not line.startswith('Usage:'):  # Non-empty and not usage line
            commands.append(line.split()[0])  # First word is the command

    # Generate bash completion script
    completion_script = """
# Bash completion for borgmatic
_borgmatic_completion() {
    local commands
    local options

    commands=(
"""
    for command in commands:
        completion_script += f"        {command}\n"
    
    completion_script += """
    )

    options=(
"""
    for option in options:
        completion_script += f"        {option}\n"
    
    completion_script += """
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
"""
    return completion_script