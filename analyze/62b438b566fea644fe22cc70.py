def bash_completion():
    return '''
# Borgmatic bash completion script
_borgmatic()
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="init create prune check list info mount extract export-tar serve umount config validate"

    # Handle options that take arguments
    case "${prev}" in
        --config|-c)
            _filedir
            return 0
            ;;
        --repository)
            _filedir
            return 0
            ;;
        --archive)
            return 0
            ;;
        *)
            ;;
    esac

    # Handle general options
    if [[ ${cur} == -* ]] ; then
        COMPREPLY=( $(compgen -W "--help --verbosity --config --repository --archive" -- ${cur}) )
        return 0
    fi

    # Complete borgmatic commands
    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
}

complete -F _borgmatic borgmatic
'''