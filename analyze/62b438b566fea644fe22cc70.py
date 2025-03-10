import subprocess

def bash_completion():
    """
    Restituisci uno script bash di completamento per il comando "borgmatic". Genera questo script analizzando i parser degli argomenti della riga di comando di "borgmatic".
    """
    # Ottieni l'output di 'borgmatic --help' per analizzare i comandi disponibili
    result = subprocess.run(['borgmatic', '--help'], capture_output=True, text=True)
    help_output = result.stdout

    # Estrai i comandi e le opzioni dall'output
    commands = []
    options = []
    for line in help_output.splitlines():
        if line.strip().startswith('-'):
            options.append(line.strip().split()[0])
        elif line.strip() and not line.strip().startswith(' '):
            commands.append(line.strip().split()[0])

    # Genera lo script di completamento bash
    script = """
_borgmatic_completion() {
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="{}"
    commands="{}"

    if [[ ${cur} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    else
        COMPREPLY=( $(compgen -W "${commands}" -- ${cur}) )
        return 0
    fi
}

complete -F _borgmatic_completion borgmatic
""".format(" ".join(options), " ".join(commands))

    return script