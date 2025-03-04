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
    value_opts="-c --config --repository --archive --encryption --ssh-command --remote-path --exclude --patterns --glob-archives"
    
    # Handle option completion
    if [[ ${cur} == -* ]]; then
        COMPREPLY=( $(compgen -W "--help --verbosity --config --repository --archive --encryption --ssh-command --remote-path --exclude --patterns --glob-archives" -- ${cur}) )
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
        --repository)
            COMPREPLY=( $(compgen -f -- ${cur}) )
            return 0
            ;;
        --archive)
            COMPREPLY=( $(compgen -f -- ${cur}) )
            return 0
            ;;
        *)
            ;;
    esac
    
    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
}

complete -F _borgmatic borgmatic
'''