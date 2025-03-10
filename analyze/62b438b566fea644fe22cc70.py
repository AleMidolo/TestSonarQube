def bash_completion():
    """
    通过检查 borgmatic 的命令行参数解析器生成 borgmatic 命令。

    返回一个用于 borgmatic 命令的 bash 补全脚本。通过检查 borgmatic 的命令行参数解析器生成此脚本。
    """
    import argparse
    import subprocess

    # 创建参数解析器
    parser = argparse.ArgumentParser(description='Generate bash completion script for borgmatic.')
    parser.add_argument('--generate-bash-completion', action='store_true', help='Generate bash completion script.')

    # 解析命令行参数
    args = parser.parse_args()

    if args.generate_bash_completion:
        # 生成 bash 补全脚本
        completion_script = """
        _borgmatic_completion() {
            local cur prev opts
            COMPREPLY=()
            cur="${COMP_WORDS[COMP_CWORD]}"
            prev="${COMP_WORDS[COMP_CWORD-1]}"
            opts=$(borgmatic --help | grep -oP '--\\K\\w+')

            if [[ ${cur} == -* ]]; then
                COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
                return 0
            fi
        }
        complete -F _borgmatic_completion borgmatic
        """
        return completion_script
    else:
        return "Usage: borgmatic --generate-bash-completion"