import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).

    :param commands: List of commands to execute.
    :param args: List of arguments to pass to the commands.
    :param cwd: Current working directory for the command (default is None).
    :param verbose: If True, print the command and its output (default is False).
    :param hide_stderr: If True, suppress stderr output (default is False).
    :param env: Environment variables to pass to the command (default is None).
    :return: The return code of the command.
    """
    full_command = commands + args
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
            print("stdout:")
            print(stdout)
        if stderr and not hide_stderr:
            print("stderr:")
            print(stderr)
    
    return process.returncode