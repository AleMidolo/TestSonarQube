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

    # Complete with commands if no other matches
    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
}

complete -F _borgmatic borgmatic
'''