import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    दिए गए कमांड(s) को चलाएं।
    """
    command_list = commands if isinstance(commands, list) else [commands]
    command_list.extend(args)
    
    stderr = subprocess.DEVNULL if hide_stderr else None
    
    if verbose:
        print(f"Running command: {' '.join(command_list)}")
    
    result = subprocess.run(
        command_list,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=stderr,
        text=True
    )
    
    if verbose:
        print(f"Command output: {result.stdout}")
    
    return result