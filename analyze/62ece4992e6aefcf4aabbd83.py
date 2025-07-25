import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    提供了一组命令。使用子进程运行给定的命令及其参数。返回运行结果（标准输出和返回码）。

    调用给定的命令。
    """
    command = commands + args
    stderr = subprocess.PIPE if hide_stderr else None
    
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            env=env,
            stdout=subprocess.PIPE,
            stderr=stderr,
            text=True,
            check=False
        )
        if verbose:
            print(f"Command: {' '.join(command)}")
            print(f"Return code: {result.returncode}")
            print(f"Output: {result.stdout}")
        
        return result.stdout, result.returncode
    except subprocess.CalledProcessError as e:
        if verbose:
            print(f"Command failed with return code {e.returncode}")
            print(f"Output: {e.stdout}")
            print(f"Error: {e.stderr}")
        return e.stdout, e.returncode