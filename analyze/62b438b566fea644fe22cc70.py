def bash_completion():
    return '''
# Borgmatic bash completion script
_borgmatic()
{
    local cur prev words cword
    _init_completion || return

    # List of all available commands
    local commands="init create prune check config list info mount umount extract export-tar restore"
    
    # Handle command completion
    if [ $cword -eq 1 ]; then
        COMPREPLY=( $(compgen -W "$commands" -- "$cur") )
        return 0
    fi

    # Handle options based on command
    case ${words[1]} in
        create)
            COMPREPLY=( $(compgen -W "--help --config --verbosity --list --stats --progress --dry-run" -- "$cur") )
            ;;
        prune)
            COMPREPLY=( $(compgen -W "--help --config --verbosity --list --stats --dry-run" -- "$cur") )
            ;;
        check)
            COMPREPLY=( $(compgen -W "--help --config --verbosity --repository --archives --prefix" -- "$cur") )
            ;;
        mount)
            COMPREPLY=( $(compgen -W "--help --config --verbosity --archive --mount-point --foreground" -- "$cur") )
            ;;
        *)
            COMPREPLY=( $(compgen -W "--help --config --verbosity" -- "$cur") )
            ;;
    esac

    return 0
}

complete -F _borgmatic borgmatic
'''