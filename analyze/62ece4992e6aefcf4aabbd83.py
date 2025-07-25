import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    दिए गए कमांड(s) को कॉल करें।
    """
    command_list = commands if isinstance(commands, list) else [commands]
    full_command = command_list + args
    
    stderr = subprocess.DEVNULL if hide_stderr else None
    
    if verbose:
        print(f"Running command: {' '.join(full_command)}")
    
    result = subprocess.run(
        full_command,
        cwd=cwd,
        env=env,
        stderr=stderr,
        stdout=subprocess.PIPE,
        text=True
    )
    
    if verbose:
        print(f"Command output: {result.stdout}")
    
    return result