import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).

    :param commands: List of commands to execute.
    :param args: List of arguments to pass to the commands.
    :param cwd: Current working directory for the command execution.
    :param verbose: If True, print the command being executed.
    :param hide_stderr: If True, suppress stderr output.
    :param env: Environment variables to use for the command execution.
    :return: The return code of the command execution.
    """
    full_command = commands + args
    if verbose:
        print(f"Executing: {' '.join(full_command)}")
    
    stderr = subprocess.DEVNULL if hide_stderr else None
    
    process = subprocess.Popen(
        full_command,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=stderr
    )
    
    stdout, _ = process.communicate()
    
    if verbose:
        print(stdout.decode())
    
    return process.returncode