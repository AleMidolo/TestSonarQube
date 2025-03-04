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
    
    # List of options that take arguments
    arg_opts="--config --repository --archive --encryption --ssh-command --remote-path --exclude --patterns --compression"
    
    # Handle option completion
    if [[ ${cur} == -* ]]; then
        COMPREPLY=( $(compgen -W "--help --verbosity --list-archives --dry-run --stats ${arg_opts}" -- ${cur}) )
        return 0
    fi
    
    # Handle command completion
    if [[ ${COMP_CWORD} -eq 1 ]]; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi
    
    # Handle argument completion for specific options
    case "${prev}" in
        --config)
            COMPREPLY=( $(compgen -f -X '!*.yaml' -- ${cur}) )
            return 0
            ;;
        --repository)
            COMPREPLY=( $(compgen -f -- ${cur}) )
            return 0
            ;;
        --archive)
            # Could potentially list actual archives here, but would need borg list output
            return 0
            ;;
        --encryption)
            COMPREPLY=( $(compgen -W "none repokey keyfile repokey-blake2 keyfile-blake2" -- ${cur}) )
            return 0
            ;;
        *)
            ;;
    esac
    
    return 0
}

complete -F _borgmatic borgmatic
'''