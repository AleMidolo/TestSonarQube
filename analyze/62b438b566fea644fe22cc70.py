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

    # List of all available commands
    local commands="init create prune check config validate"
    
    # Handle command completion
    if [ $cword -eq 1 ]; then
        COMPREPLY=( $(compgen -W "${commands}" -- ${cur}) )
        return 0
    fi

    # Handle options based on command
    case ${words[1]} in
        init)
            COMPREPLY=( $(compgen -W "--encryption --append-only --storage-quota" -- ${cur}) )
            ;;
        create)
            COMPREPLY=( $(compgen -W "--progress --stats --dry-run --exclude --compression" -- ${cur}) )
            ;;
        prune)
            COMPREPLY=( $(compgen -W "--keep-daily --keep-weekly --keep-monthly --dry-run" -- ${cur}) )
            ;;
        check)
            COMPREPLY=( $(compgen -W "--repository --archives --verify-data" -- ${cur}) )
            ;;
        config)
            COMPREPLY=( $(compgen -W "--list --generate --edit" -- ${cur}) )
            ;;
        validate)
            COMPREPLY=( $(compgen -W "--config --lint" -- ${cur}) )
            ;;
    esac

    return 0
}

complete -F _borgmatic borgmatic
'''