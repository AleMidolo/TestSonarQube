import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).

    :param commands: List of commands to execute.
    :param args: List of arguments to pass to the command.
    :param cwd: Current working directory for the command (optional).
    :param verbose: If True, print the command before executing (optional).
    :param hide_stderr: If True, suppress stderr output (optional).
    :param env: Environment variables to pass to the command (optional).
    :return: The return code of the command.
    """
    full_command = commands + args
    if verbose:
        print(f"Running command: {' '.join(full_command)}")
    
    stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
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
            print(stdout)
        if stderr and not hide_stderr:
            print(stderr)
    
    return process.returncode