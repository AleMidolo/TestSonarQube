def bash_completion():
    """
    Return a bash completion script for the borgmatic command. Produce this by introspecting
    borgmatic's command-line argument parsers.
    """
    return '''
_borgmatic()
{
    local cur prev words cword
    _init_completion || return

    # List of all available borgmatic commands
    local commands="init create prune check config validate generate-key list info export-tar extract mount umount"
    
    # Handle command completion
    if [ $cword -eq 1 ]; then
        COMPREPLY=( $(compgen -W "$commands" -- "$cur") )
        return 0
    fi

    # Handle options based on command
    case ${words[1]} in
        create)
            COMPREPLY=( $(compgen -W "--config --verbosity --json --dry-run --monitoring-verbosity" -- "$cur") )
            ;;
        prune)
            COMPREPLY=( $(compgen -W "--config --verbosity --json --dry-run --monitoring-verbosity" -- "$cur") )
            ;;
        check)
            COMPREPLY=( $(compgen -W "--config --verbosity --json --only --monitoring-verbosity" -- "$cur") )
            ;;
        list|info)
            COMPREPLY=( $(compgen -W "--config --verbosity --json --archive" -- "$cur") )
            ;;
        mount)
            COMPREPLY=( $(compgen -W "--config --verbosity --json --archive --mount-point" -- "$cur") )
            ;;
        *)
            COMPREPLY=( $(compgen -W "--config --verbosity --json" -- "$cur") )
            ;;
    esac

    # Handle file completion for --config option
    if [[ $prev == "--config" ]]; then
        _filedir yaml
        return 0
    fi

    return 0
}

complete -F _borgmatic borgmatic
'''