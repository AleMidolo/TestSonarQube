def bash_completion():
    """
    通过检查 borgmatic 的命令行参数解析器生成 borgmatic 命令。

    返回一个用于 borgmatic 命令的 bash 补全脚本。通过检查 borgmatic 的命令行参数解析器生成此脚本。
    """
    import subprocess

    # Generate the bash completion script using borgmatic's command line interface
    try:
        completion_script = subprocess.check_output(['borgmatic', 'completion', 'bash'], text=True)
        return completion_script
    except subprocess.CalledProcessError as e:
        return f"Error generating completion script: {e}"