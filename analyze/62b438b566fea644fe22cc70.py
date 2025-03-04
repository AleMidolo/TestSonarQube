def bash_completion():
    """
    通过检查 borgmatic 的命令行参数解析器生成 borgmatic 命令。

    返回一个用于 borgmatic 命令的 bash 补全脚本。通过检查 borgmatic 的命令行参数解析器生成此脚本。
    """
    completion_script = '''
_borgmatic()
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    
    # 主要命令选项
    opts="init create prune check list info export-tar extract mount umount config validate"
    
    # 通用选项
    common_opts="--config --verbosity --syslog-verbosity --log-file --monitoring-verbosity --help"
    
    # 根据前一个单词提供不同的补全
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
            COMPREPLY=( $(compgen -W "0 1 2 3" -- ${cur}) )
            return 0
            ;;
        *)
            # 如果是以破折号开头，则提供通用选项
            if [[ ${cur} == -* ]] ; then
                COMPREPLY=( $(compgen -W "${common_opts}" -- ${cur}) )
                return 0
            fi
            
            # 否则提供主要命令
            COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
            return 0
            ;;
    esac
}

complete -F _borgmatic borgmatic
'''
    return completion_script