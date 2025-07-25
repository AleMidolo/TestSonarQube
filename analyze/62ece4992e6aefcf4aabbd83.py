import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Esegui il/i comando/i fornito/i.
    """
    if isinstance(commands, str):
        commands = [commands]
    
    full_command = commands + args
    
    stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
    
    process = subprocess.Popen(
        full_command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=stderr,
        env=env,
        text=True
    )
    
    stdout, stderr = process.communicate()
    
    if verbose:
        print(f"Command: {' '.join(full_command)}")
        if stdout:
            print(f"Stdout: {stdout}")
        if stderr and not hide_stderr:
            print(f"Stderr: {stderr}")
    
    return process.returncode, stdout, stderr