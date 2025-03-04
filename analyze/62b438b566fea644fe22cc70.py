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
    
    # List of options that take config file paths
    config_opts="-c --config --borgmatic-source-directory"
    
    # Handle completion for different cases
    case "${prev}" in
        borgmatic)
            COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
            return 0
            ;;
        -c|--config)
            COMPREPLY=( $(compgen -f -X '!*.yaml' -- ${cur}) )
            return 0
            ;;
        --borgmatic-source-directory)
            COMPREPLY=( $(compgen -d -- ${cur}) )
            return 0
            ;;
        *)
            # If current word starts with -, complete with options
            if [[ ${cur} == -* ]] ; then
                COMPREPLY=( $(compgen -W "${config_opts}" -- ${cur}) )
                return 0
            fi
            ;;
    esac
    
    # Default to completing files
    COMPREPLY=( $(compgen -f -- ${cur}) )
    return 0
}

complete -F _borgmatic borgmatic
'''