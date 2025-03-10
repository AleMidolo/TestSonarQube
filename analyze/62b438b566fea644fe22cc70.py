import subprocess

def bash_completion():
    """
    Restituisci uno script bash di completamento per il comando "borgmatic". Genera questo script analizzando i parser degli argomenti della riga di comando di "borgmatic".
    """
    # Ottieni l'output di 'borgmatic --help' per analizzare i comandi disponibili
    result = subprocess.run(['borgmatic', '--help'], capture_output=True, text=True)
    help_output = result.stdout

    # Estrai i comandi disponibili dall'output di help
    commands = []
    for line in help_output.splitlines():
        if line.strip().startswith('-'):
            command = line.split()[0]
            commands.append(command)

    # Genera lo script di completamento bash
    bash_script = """
_borgmatic_completion() {
    local cur prev commands
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    commands="%s"

    if [[ ${cur} == -* ]]; then
        COMPREPLY=( $(compgen -W "${commands}" -- ${cur}) )
        return 0
    fi
}

complete -F _borgmatic_completion borgmatic
""" % " ".join(commands)

    return bash_script