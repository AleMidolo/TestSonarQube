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
    stderr = subprocess.DEVNULL if hide_stderr else None
    
    if verbose:
        print(f"Running command: {' '.join(full_command)}")
    
    result = subprocess.run(
        full_command,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE if verbose else None,
        stderr=stderr,
        text=True
    )
    
    if verbose and result.stdout:
        print(result.stdout)
    
    return result.returncode