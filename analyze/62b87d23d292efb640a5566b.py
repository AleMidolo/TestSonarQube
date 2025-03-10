import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    दिए गए कमांड(s) को चलाएं।
    """
    command_list = commands if isinstance(commands, list) else [commands]
    full_command = command_list + args
    
    stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
    
    if verbose:
        print(f"Running command: {' '.join(full_command)}")
    
    result = subprocess.run(
        full_command,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=stderr,
        text=True
    )
    
    if verbose:
        print(f"Command output: {result.stdout}")
        if not hide_stderr:
            print(f"Command error output: {result.stderr}")
    
    return result