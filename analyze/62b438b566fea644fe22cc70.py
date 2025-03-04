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
    opts="init create check prune list info export-tar extract mount umount config validate"
    
    # 通用选项
    common_opts="--config --verbosity --log-file --help --version"
    
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
        --verbosity)
            COMPREPLY=( $(compgen -W "0 1 2" -- ${cur}) )
            return 0
            ;;
        --log-file)
            COMPREPLY=( $(compgen -f -- ${cur}) )
            return 0
            ;;
        *)
            # 如果当前输入以破折号开头，则提供通用选项
            if [[ ${cur} == -* ]] ; then
                COMPREPLY=( $(compgen -W "${common_opts}" -- ${cur}) )
                return 0
            fi
            ;;
    esac
    
    # 默认补全为命令选项
    COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
    return 0
}

complete -F _borgmatic borgmatic
'''
    return completion_script