import subprocess
import os

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    दिए गए कमांड(s) को कॉल करें।
    """
    if isinstance(commands, str):
        commands = [commands]
    
    full_command = [cmd.format(*args) for cmd in commands]
    
    if verbose:
        print("Running command:", ' '.join(full_command))
    
    stderr = subprocess.DEVNULL if hide_stderr else None
    
    result = subprocess.run(full_command, cwd=cwd, env=env, stderr=stderr)
    
    return result.returncode