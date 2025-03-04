def bash_completion():
    """
    Restituisci uno script bash di completamento per il comando "borgmatic". Genera questo script analizzando i parser degli argomenti della riga di comando di "borgmatic".
    """
    completion_script = """
    _borgmatic_completion() {
        local cur prev opts
        COMPREPLY=()
        cur="${COMP_WORDS[COMP_CWORD]}"
        prev="${COMP_WORDS[COMP_CWORD-1]}"
        opts=$(borgmatic --help | grep -oP '(?<=^  )\w+')

        if [[ ${cur} == -* ]]; then
            COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        else
            COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        fi
    }

    complete -F _borgmatic_completion borgmatic
    """
    return completion_script