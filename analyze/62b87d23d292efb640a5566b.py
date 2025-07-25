import subprocess
import os

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).
    """
    if cwd is None:
        cwd = os.getcwd()
    
    if env is None:
        env = os.environ.copy()
    
    if isinstance(commands, str):
        commands = [commands]
    
    results = []
    
    for command in commands:
        full_command = [command] + args
        if verbose:
            print(f"Running command: {' '.join(full_command)} in {cwd}")
        
        stderr = subprocess.DEVNULL if hide_stderr else None
        
        result = subprocess.run(full_command, cwd=cwd, env=env, stderr=stderr)
        results.append(result)
    
    return results