import subprocess
import os

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Llama al/los comando(s) dado(s).
    """
    if isinstance(commands, str):
        commands = [commands]
    
    results = []
    for command in commands:
        full_command = [command] + args
        if verbose:
            print(f"Running command: {' '.join(full_command)}")
        
        process = subprocess.Popen(
            full_command,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE if not hide_stderr else subprocess.DEVNULL,
            env=env
        )
        
        stdout, stderr = process.communicate()
        results.append({
            'command': command,
            'returncode': process.returncode,
            'stdout': stdout.decode('utf-8'),
            'stderr': stderr.decode('utf-8') if not hide_stderr else None
        })
    
    return results