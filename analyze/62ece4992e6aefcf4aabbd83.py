import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    提供了一组命令。使用子进程运行给定的命令及其参数。返回运行结果（标准输出和返回码）。

    调用给定的命令。
    """
    command = [commands] + list(args)
    if verbose:
        print(f"Running command: {' '.join(command)}")
    
    stderr = subprocess.STDOUT if hide_stderr else subprocess.PIPE
    
    result = subprocess.run(command, cwd=cwd, stdout=subprocess.PIPE, stderr=stderr, env=env, text=True)
    
    return result.stdout, result.returncode