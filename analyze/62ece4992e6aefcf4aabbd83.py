import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    提供了一组命令。使用子进程运行给定的命令及其参数。返回运行结果（标准输出和返回码）。

    调用给定的命令。
    """
    command = commands + args
    stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
    process = subprocess.Popen(
        command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=stderr,
        env=env,
        text=True
    )
    stdout, stderr = process.communicate()
    
    if verbose:
        print(f"Command: {' '.join(command)}")
        print(f"Stdout: {stdout}")
        if stderr:
            print(f"Stderr: {stderr}")
    
    return stdout, process.returncode