def bash_completion():
    return '''
_borgmatic()
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    
    # Main borgmatic commands
    opts="init create prune list info check extract mount umount rcreate rlist rinfo rdelete config validate"

    # Common options
    common_opts="--config --verbosity --syslog-verbosity --json --help --version"
    
    case "${prev}" in
        borgmatic)
            COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
            return 0
            ;;
        --config)
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

    # Handle options
    if [[ ${cur} == -* ]] ; then
        case "${COMP_WORDS[1]}" in
            create)
                COMPREPLY=( $(compgen -W "${common_opts} --progress --stats --list --dry-run" -- ${cur}) )
                ;;
            prune)
                COMPREPLY=( $(compgen -W "${common_opts} --list --dry-run" -- ${cur}) )
                ;;
            list|info)
                COMPREPLY=( $(compgen -W "${common_opts} --archive --json" -- ${cur}) )
                ;;
            check)
                COMPREPLY=( $(compgen -W "${common_opts} --progress --repair --only-checks" -- ${cur}) )
                ;;
            extract)
                COMPREPLY=( $(compgen -W "${common_opts} --archive --path --destination --progress --strip-components" -- ${cur}) )
                ;;
            mount)
                COMPREPLY=( $(compgen -W "${common_opts} --archive --path --mount-point --foreground" -- ${cur}) )
                ;;
            *)
                COMPREPLY=( $(compgen -W "${common_opts}" -- ${cur}) )
                ;;
        esac
        return 0
    fi

    # Complete files/directories if no other matches
    COMPREPLY=( $(compgen -f -- ${cur}) )
    return 0
}

complete -F _borgmatic borgmatic
'''