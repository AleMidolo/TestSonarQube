def bash_completion():
    return '''
_borgmatic()
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    
    # Main borgmatic commands
    opts="init create prune list info check extract export-tar mount umount rcreate rinfo rlist rdelete config validate"

    # Common options
    common_opts="-h --help -c --config --verbosity --syslog-verbosity"

    case "${prev}" in
        borgmatic)
            COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
            return 0
            ;;
        -c|--config)
            COMPREPLY=( $(compgen -f -- ${cur}) )
            return 0
            ;;
        --verbosity|--syslog-verbosity)
            COMPREPLY=( $(compgen -W "0 1 2 3" -- ${cur}) )
            return 0
            ;;
        *)
            ;;
    esac

    if [[ ${cur} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${common_opts}" -- ${cur}) )
        return 0
    fi

    # Command-specific options
    case "${COMP_WORDS[1]}" in
        create)
            COMPREPLY=( $(compgen -W "--list --stats --json" -- ${cur}) )
            ;;
        prune)
            COMPREPLY=( $(compgen -W "--list --stats --json" -- ${cur}) )
            ;;
        list)
            COMPREPLY=( $(compgen -W "--archive --json --format" -- ${cur}) )
            ;;
        info)
            COMPREPLY=( $(compgen -W "--archive --json" -- ${cur}) )
            ;;
        check)
            COMPREPLY=( $(compgen -W "--archive --verify-data --json" -- ${cur}) )
            ;;
        extract)
            COMPREPLY=( $(compgen -W "--archive --path --destination --json" -- ${cur}) )
            ;;
        mount)
            COMPREPLY=( $(compgen -W "--archive --path --mount-point --json" -- ${cur}) )
            ;;
        *)
            ;;
    esac
}

complete -F _borgmatic borgmatic
'''