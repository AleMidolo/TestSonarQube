import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    दिए गए कमांड(s) को कॉल करें।
    """
    command_list = commands if isinstance(commands, list) else [commands]
    full_command = command_list + args
    
    stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
    
    if verbose:
        print(f"Running command: {' '.join(full_command)}")
    
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
        if stdout:
            print(f"stdout:\n{stdout}")
        if stderr and not hide_stderr:
            print(f"stderr:\n{stderr}")
    
    return process.returncode, stdout, stderr