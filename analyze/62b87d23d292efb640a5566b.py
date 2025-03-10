import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    执行指定的命令。

    :param commands: 要执行的命令列表。
    :param args: 命令的参数列表。
    :param cwd: 执行命令的工作目录。如果为None，则使用当前工作目录。
    :param verbose: 是否打印命令执行的详细信息。
    :param hide_stderr: 是否隐藏标准错误输出。
    :param env: 环境变量字典。如果为None，则使用当前环境变量。
    :return: 命令执行的返回码。
    """
    full_command = commands + args
    stderr = subprocess.DEVNULL if hide_stderr else None
    
    if verbose:
        print(f"Running command: {' '.join(full_command)}")
        if cwd:
            print(f"Working directory: {cwd}")
        if env:
            print(f"Environment variables: {env}")
    
    process = subprocess.Popen(
        full_command,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=stderr,
        text=True
    )
    
    stdout, _ = process.communicate()
    
    if verbose:
        print(f"Command output:\n{stdout}")
    
    return process.returncode