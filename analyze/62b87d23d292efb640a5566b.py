import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).

    :param commands: List of commands to execute.
    :param args: List of arguments to pass to the commands.
    :param cwd: Current working directory for the command (optional).
    :param verbose: If True, print the command and its output (optional).
    :param hide_stderr: If True, suppress stderr output (optional).
    :param env: Environment variables to pass to the command (optional).
    :return: The output of the command.
    """
    full_command = commands + args
    stderr = subprocess.PIPE if hide_stderr else None
    
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
    
    return result.stdout