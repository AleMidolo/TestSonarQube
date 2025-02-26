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
        
        process = subprocess.Popen(full_command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE if not hide_stderr else subprocess.DEVNULL, env=env)
        stdout, stderr = process.communicate()
        
        if process.returncode != 0:
            raise subprocess.CalledProcessError(process.returncode, full_command, output=stdout, stderr=stderr)
        
        output.append(stdout.decode('utf-8'))
    
    return output