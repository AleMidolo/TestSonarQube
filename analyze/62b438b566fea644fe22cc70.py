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

    if [[ ${cur} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${common_opts}" -- ${cur}) )
        return 0
    fi

    # Complete subcommands
    case "${COMP_WORDS[1]}" in
        create)
            local create_opts="--progress --stats --dry-run"
            COMPREPLY=( $(compgen -W "${create_opts} ${common_opts}" -- ${cur}) )
            ;;
        prune)
            local prune_opts="--stats --dry-run"
            COMPREPLY=( $(compgen -W "${prune_opts} ${common_opts}" -- ${cur}) )
            ;;
        list|info)
            local list_opts="--archive --json"
            COMPREPLY=( $(compgen -W "${list_opts} ${common_opts}" -- ${cur}) )
            ;;
        check)
            local check_opts="--progress --repair --only-checks"
            COMPREPLY=( $(compgen -W "${check_opts} ${common_opts}" -- ${cur}) )
            ;;
        extract)
            local extract_opts="--archive --path --destination --progress --dry-run"
            COMPREPLY=( $(compgen -W "${extract_opts} ${common_opts}" -- ${cur}) )
            ;;
        mount)
            local mount_opts="--archive --path --mount-point --foreground"
            COMPREPLY=( $(compgen -W "${mount_opts} ${common_opts}" -- ${cur}) )
            ;;
        *)
            COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
            ;;
    esac

    return 0
}

complete -F _borgmatic borgmatic
'''