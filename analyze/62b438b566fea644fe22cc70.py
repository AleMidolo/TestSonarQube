def bash_completion():
    """
    Devuelve un script de autocompletado para bash para el comando de borgmatic. Esto se genera mediante la introspección de los analizadores de argumentos de línea de comandos de borgmatic.
    """
    return '''
_borgmatic()
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="--config --help --version init create check extract list info mount umount prune"

    case "${prev}" in
        --config)
            _filedir
            return 0
            ;;
        mount)
            _filedir -d
            return 0
            ;;
        extract)
            _filedir -d
            return 0
            ;;
        *)
            ;;
    esac

    if [[ ${cur} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi

    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
}

complete -F _borgmatic borgmatic
'''