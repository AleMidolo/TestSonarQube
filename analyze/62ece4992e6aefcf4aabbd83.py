import subprocess
import os

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).
    """
    if isinstance(commands, str):
        commands = [commands]
    
    output = []
    for command in commands:
        full_command = [command] + args
        if verbose:
            print(f"Running command: {' '.join(full_command)}")
        
        result = subprocess.run(
            full_command,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE if not hide_stderr else subprocess.DEVNULL,
            env=env
        )
        
        output.append(result.stdout.decode('utf-8'))
        
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, full_command, output=result.stderr.decode('utf-8'))
    
    return output