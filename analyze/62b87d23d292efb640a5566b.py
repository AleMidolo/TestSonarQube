import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    दिए गए कमांड(s) को चलाएं।
    """
    command_list = commands if isinstance(commands, list) else [commands]
    command_list.extend(args)
    
    stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
    
    process = subprocess.Popen(
        command_list,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=stderr,
        env=env,
        text=True
    )
    
    stdout, stderr = process.communicate()
    
    if verbose:
        print(f"Command: {' '.join(command_list)}")
        print(f"Working Directory: {cwd}")
        print(f"Environment: {env}")
        print(f"Output:\n{stdout}")
        if stderr:
            print(f"Errors:\n{stderr}")
    
    return process.returncode, stdout, stderr