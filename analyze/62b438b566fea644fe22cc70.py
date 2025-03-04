def bash_completion():
    return '''
# borgmatic bash completion script
_borgmatic()
{
    local cur prev words cword
    _init_completion || return

    # Complete subcommands
    if [[ $cword -eq 1 ]]; then
        COMPREPLY=( $( compgen -W "init create prune check list info mount extract export-tar serve config validate" -- "$cur" ) )
        return 0
    fi

    # Complete options based on subcommand
    case ${words[1]} in
        create)
            COMPREPLY=( $( compgen -W "--config --excludes --help --json --list --progress --stats" -- "$cur" ) )
            ;;
        prune) 
            COMPREPLY=( $( compgen -W "--config --help --list --stats" -- "$cur" ) )
            ;;
        check)
            COMPREPLY=( $( compgen -W "--config --help --json --progress --repair" -- "$cur" ) )
            ;;
        list|info)
            COMPREPLY=( $( compgen -W "--config --help --json" -- "$cur" ) )
            ;;
        mount)
            COMPREPLY=( $( compgen -W "--config --help --mount-point --archive" -- "$cur" ) )
            ;;
        extract)
            COMPREPLY=( $( compgen -W "--config --help --archive --path" -- "$cur" ) )
            ;;
        export-tar)
            COMPREPLY=( $( compgen -W "--config --help --archive --tar" -- "$cur" ) )
            ;;
        serve)
            COMPREPLY=( $( compgen -W "--config --help" -- "$cur" ) )
            ;;
        config|validate)
            COMPREPLY=( $( compgen -W "--config --help" -- "$cur" ) )
            ;;
    esac

    return 0
}

complete -F _borgmatic borgmatic
'''