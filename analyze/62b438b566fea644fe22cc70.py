def bash_completion():
    """
    Restituisci uno script bash di completamento per il comando "borgmatic". Genera questo script analizzando i parser degli argomenti della riga di comando di "borgmatic".
    """
    completion_script = """
    _borgmatic_completion() {
        local cur prev words cword
        _init_completion || return

        case "$prev" in
            --config)
                COMPREPLY=( $(compgen -f -- "$cur") )
                return 0
                ;;
            --repository)
                COMPREPLY=( $(compgen -f -- "$cur") )
                return 0
                ;;
            *)
                COMPREPLY=( $(compgen -W "init config run" -- "$cur") )
                return 0
                ;;
        esac
    }

    complete -F _borgmatic_completion borgmatic
    """
    return completion_script