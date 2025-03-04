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
    
    # Si es el primer argumento o empieza con guión
    if [[ ${COMP_CWORD} -eq 1 ]] || [[ ${cur} == -* ]] ; then
        COMPREPLY=( $(compgen -W "${opts} ${common_opts}" -- ${cur}) )
        return 0
    fi
    
    # Autocompletado específico según el subcomando
    case "${COMP_WORDS[1]}" in
        init)
            COMPREPLY=( $(compgen -W "--encryption --append-only" -- ${cur}) )
            ;;
        create)
            COMPREPLY=( $(compgen -W "--progress --stats --json --dry-run" -- ${cur}) )
            ;;
        check)
            COMPREPLY=( $(compgen -W "--repository --archive --only --last --prefix" -- ${cur}) )
            ;;
        prune)
            COMPREPLY=( $(compgen -W "--keep-daily --keep-weekly --keep-monthly --stats" -- ${cur}) )
            ;;
        list|info)
            COMPREPLY=( $(compgen -W "--archive --json --prefix" -- ${cur}) )
            ;;
        mount)
            COMPREPLY=( $(compgen -W "--archive --mount-point --foreground" -- ${cur}) )
            ;;
        *)
            ;;
    esac
    
    return 0
}

complete -F _borgmatic borgmatic
'''