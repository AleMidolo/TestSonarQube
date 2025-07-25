import subprocess
import os

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).
    """
    if isinstance(commands, str):
        commands = [commands]
    
    if cwd is None:
        cwd = os.getcwd()
    
    for command in commands:
        full_command = [command] + args
        if verbose:
            print(f"Running command: {' '.join(full_command)} in {cwd}")
        
        with open(os.devnull, 'w') as devnull:
            stderr = subprocess.DEVNULL if hide_stderr else None
            result = subprocess.run(full_command, cwd=cwd, env=env, stderr=stderr)
        
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, full_command)