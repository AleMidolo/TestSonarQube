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
    
    # Lista de opciones y subcomandos principales
    opts="init create check prune list info mount extract export-tar rcreate rinfo rlist rdelete config validate generate-key"
    
    # Opciones comunes
    common_opts="--config --verbosity --syslog-verbosity --log-file --monitoring-verbosity --help"
    
    # Si estamos en el primer argumento o después de un guión
    if [[ ${cur} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${common_opts}" -- ${cur}) )
        return 0
    fi
    
    # Autocompletado de subcomandos
    case "${prev}" in
        borgmatic)
            COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
            return 0
            ;;
        --config)
            COMPREPLY=( $(compgen -f -- ${cur}) )
            return 0
            ;;
        --log-file)
            COMPREPLY=( $(compgen -f -- ${cur}) )
            return 0
            ;;
        *)
            ;;
    esac
    
    # Autocompletado de archivos por defecto
    COMPREPLY=( $(compgen -f ${cur}) )
    return 0
}

complete -F _borgmatic borgmatic
'''