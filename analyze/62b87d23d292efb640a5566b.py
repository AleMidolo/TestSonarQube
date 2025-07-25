import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Llama al/los comando(s) dado(s).
    """
    if isinstance(commands, str):
        commands = [commands]
    
    full_command = commands + args
    
    stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
    
    try:
        result = subprocess.run(
            full_command,
            cwd=cwd,
            env=env,
            stdout=subprocess.PIPE,
            stderr=stderr,
            text=True,
            check=True
        )
        
        if verbose:
            print(f"Command executed: {' '.join(full_command)}")
            print(f"Output: {result.stdout}")
        
        return result.stdout
    
    except subprocess.CalledProcessError as e:
        if verbose:
            print(f"Command failed: {' '.join(full_command)}")
            print(f"Error: {e.stderr}")
        raise