import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).

    :param commands: List of commands to execute.
    :param args: List of arguments to pass to the commands.
    :param cwd: Current working directory for the command (default: None).
    :param verbose: If True, print the command and its output (default: False).
    :param hide_stderr: If True, suppress stderr output (default: False).
    :param env: Environment variables to pass to the command (default: None).
    :return: The return code of the command.
    """
    full_command = commands + args
    stderr = subprocess.DEVNULL if hide_stderr else None
    
    if verbose:
        print(f"Running command: {' '.join(full_command)}")
    
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
        print(f"Command output:\n{stdout}")
        if stderr and not hide_stderr:
            print(f"Command error output:\n{stderr}")
    
    return process.returncode