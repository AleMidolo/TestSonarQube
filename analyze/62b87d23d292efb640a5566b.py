import subprocess
import os

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    दिए गए कमांड(s) को चलाएं।
    """
    if cwd is None:
        cwd = os.getcwd()
    
    if env is None:
        env = os.environ

    command_list = [commands] + args
    if verbose:
        print(f"Running command: {' '.join(command_list)} in {cwd}")

    stderr = subprocess.DEVNULL if hide_stderr else None

    result = subprocess.run(command_list, cwd=cwd, env=env, stderr=stderr)
    
    return result.returncode