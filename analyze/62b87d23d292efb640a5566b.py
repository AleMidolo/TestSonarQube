import subprocess
import os

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    执行指定的命令。
    """
    if cwd is None:
        cwd = os.getcwd()
    
    if env is None:
        env = os.environ.copy()
    
    command = [commands] + args
    stderr = subprocess.DEVNULL if hide_stderr else None
    
    if verbose:
        print(f"Running command: {' '.join(command)} in {cwd}")
    
    result = subprocess.run(command, cwd=cwd, env=env, stderr=stderr)
    
    return result.returncode