import subprocess
import os

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Esegui il/i comando/i fornito/i.
    """
    if cwd is None:
        cwd = os.getcwd()
    
    if env is None:
        env = os.environ

    if isinstance(commands, str):
        commands = [commands]

    results = []
    for command in commands:
        full_command = [command] + args
        if verbose:
            print(f"Running command: {' '.join(full_command)} in {cwd}")
        
        process = subprocess.Popen(full_command, cwd=cwd, env=env, 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE if not hide_stderr else subprocess.DEVNULL)
        stdout, stderr = process.communicate()
        
        result = {
            'command': command,
            'returncode': process.returncode,
            'stdout': stdout.decode('utf-8'),
            'stderr': stderr.decode('utf-8') if not hide_stderr else None
        }
        results.append(result)

    return results