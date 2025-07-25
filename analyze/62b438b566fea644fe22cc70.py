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
    common_opts="--config --verbosity --syslog-verbosity --log-file --monitoring-verbosity \
                 --dry-run --help --version"

    # Handle different previous arguments
    case "${prev}" in
        borgmatic)
            COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
            return 0
            ;;
        --config)
            COMPREPLY=( $(compgen -f -- ${cur}) )
            return 0
            ;;
        --verbosity|--syslog-verbosity|--monitoring-verbosity)
            COMPREPLY=( $(compgen -W "CRITICAL ERROR WARNING INFO DEBUG TRACE" -- ${cur}) )
            return 0
            ;;
        create|prune|list|info|check|extract|mount)
            COMPREPLY=( $(compgen -W "${common_opts}" -- ${cur}) )
            return 0
            ;;
        *)
            # If current word starts with -, complete from common options
            if [[ ${cur} == -* ]]; then
                COMPREPLY=( $(compgen -W "${common_opts}" -- ${cur}) )
            else
                COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
            fi
            return 0
            ;;
    esac
}

complete -F _borgmatic borgmatic
'''