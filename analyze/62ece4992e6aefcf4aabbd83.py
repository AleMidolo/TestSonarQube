import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Esegui il/i comando/i fornito/i.
    """
    if isinstance(commands, str):
        commands = [commands]
    
    full_command = commands + args
    
    stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
    
    if verbose:
        print(f"Esecuzione del comando: {' '.join(full_command)}")
    
    process = subprocess.Popen(
        full_command,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=stderr,
        text=True
    )
    
    stdout, stderr = process.communicate()
    
    if verbose:
        if stdout:
            print("Output del comando:")
            print(stdout)
        if stderr and not hide_stderr:
            print("Errore del comando:")
            print(stderr)
    
    return process.returncode, stdout, stderr