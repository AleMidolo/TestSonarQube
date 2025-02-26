import subprocess
import os

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).
    """
    if isinstance(commands, str):
        commands = [commands]
    
    if env is None:
        env = os.environ.copy()
    
    for command in commands:
        full_command = [command] + args
        if verbose:
            print(f"Running command: {' '.join(full_command)}")
        
        with open(os.devnull, 'w') if hide_stderr else None as stderr:
            result = subprocess.run(full_command, cwd=cwd, env=env, stderr=stderr)
        
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, full_command)