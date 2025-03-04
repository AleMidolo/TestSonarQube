def bash_completion():
    """
    Return a bash completion script for the borgmatic command. Produce this by introspecting
    borgmatic's command-line argument parsers.
    """
    return '''
_borgmatic()
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    
    # List of all borgmatic commands
    opts="init create prune check list info export-tar extract mount umount rcreate rlist rinfo rdelete config validate generate-key"
    
    # List of options that take values
    value_opts="-c --config --repository --archive --destination --json --monitoring-verbosity --verbosity"
    
    # Handle option completion
    if [[ ${cur} == -* ]]; then
        COMPREPLY=( $(compgen -W "--help --version --borgmatic-source-directory --verbosity \
            --json --monitoring-verbosity -c --config --repository --archive \
            --destination --dry-run --progress --stats --list --files --prefix" -- ${cur}) )
        return 0
    fi
    
    # Handle command completion
    if [[ ${COMP_CWORD} -eq 1 ]]; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi
    
    # Handle value completion for specific options
    case "${prev}" in
        -c|--config)
            COMPREPLY=( $(compgen -f -- ${cur}) )
            return 0
            ;;
        --repository|--archive|--destination)
            COMPREPLY=( $(compgen -f -- ${cur}) )
            return 0
            ;;
        --verbosity|--monitoring-verbosity)
            COMPREPLY=( $(compgen -W "0 1 2" -- ${cur}) )
            return 0
            ;;
    esac
    
    return 0
}

complete -F _borgmatic borgmatic
'''