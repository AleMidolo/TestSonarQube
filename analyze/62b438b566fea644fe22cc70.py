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
    common_opts="-h --help -c --config --verbosity --syslog-verbosity"
    
    case "${prev}" in
        borgmatic)
            COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
            return 0
            ;;
        -c|--config)
            COMPREPLY=( $(compgen -f -- ${cur}) )
            return 0
            ;;
        --verbosity|--syslog-verbosity)
            COMPREPLY=( $(compgen -W "0 1 2 3" -- ${cur}) )
            return 0
            ;;
        create)
            COMPREPLY=( $(compgen -W "--progress --stats --json" -- ${cur}) )
            return 0
            ;;
        prune)
            COMPREPLY=( $(compgen -W "--stats --list --dry-run" -- ${cur}) )
            return 0
            ;;
        list|info)
            COMPREPLY=( $(compgen -W "--archive --json" -- ${cur}) )
            return 0
            ;;
        check)
            COMPREPLY=( $(compgen -W "--repository --archives --verify-data" -- ${cur}) )
            return 0
            ;;
        extract)
            COMPREPLY=( $(compgen -W "--archive --path --destination" -- ${cur}) )
            return 0
            ;;
        mount)
            COMPREPLY=( $(compgen -W "--archive --path --mount-point --foreground" -- ${cur}) )
            return 0
            ;;
        *)
            COMPREPLY=( $(compgen -W "${common_opts}" -- ${cur}) )
            return 0
            ;;
    esac
}

complete -F _borgmatic borgmatic
'''