import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    दिए गए कमांड(s) को चलाएं।
    """
    command_list = [commands] + args
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
        if stdout:
            print(f"Stdout: {stdout}")
        if stderr and not hide_stderr:
            print(f"Stderr: {stderr}")
    
    return process.returncode, stdout, stderr