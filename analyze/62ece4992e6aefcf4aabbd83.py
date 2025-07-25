import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    提供了一组命令。使用子进程运行给定的命令及其参数。返回运行结果（标准输出和返回码）。

    调用给定的命令。
    """
    command = commands + args
    stderr = subprocess.PIPE if hide_stderr else None
    
    if verbose:
        print(f"Running command: {' '.join(command)}")
    
    process = subprocess.Popen(
        command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=stderr,
        env=env,
        text=True
    )
    
    stdout, stderr = process.communicate()
    return_code = process.returncode
    
    if verbose:
        print(f"Command returned with code: {return_code}")
        if stdout:
            print(f"Standard Output:\n{stdout}")
        if stderr and not hide_stderr:
            print(f"Standard Error:\n{stderr}")
    
    return stdout, return_code