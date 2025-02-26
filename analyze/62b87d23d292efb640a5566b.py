import subprocess
import os

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).
    """
    if isinstance(commands, str):
        commands = [commands]
    
    if env is None:
        env = os.environ.copy()
    
    for command in commands:
        full_command = [command] + args
        if verbose:
            print(f"Running command: {' '.join(full_command)}")
        
        with subprocess.Popen(full_command, cwd=cwd, env=env, 
                              stdout=subprocess.PIPE, 
                              stderr=subprocess.PIPE if not hide_stderr else subprocess.DEVNULL) as process:
            stdout, stderr = process.communicate()
            if process.returncode != 0:
                print(f"Command '{command}' failed with return code {process.returncode}")
                if not hide_stderr:
                    print(stderr.decode())
            else:
                print(stdout.decode())