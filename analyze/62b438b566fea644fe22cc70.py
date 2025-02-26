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
            --archive)
                COMPREPLY=( $(compgen -W "$(borgmatic list-archives)" -- "$cur") )
                return 0
                ;;
        esac

        COMPREPLY=( $(compgen -W "--config --repository --archive --verbosity --dry-run --list --stats" -- "$cur") )
    }

    complete -F _borgmatic_completion borgmatic
    """
    return completion_script