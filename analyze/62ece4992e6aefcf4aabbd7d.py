import subprocess
import os
import sys

def subprocess_run_helper(func, *args, timeout, extra_env=None):
    if extra_env is None:
        extra_env = {}
    
    # Prepare the command to run
    command = [sys.executable, '-c', f'import {func.__module__}; {func.__module__}.{func.__name__}(*{args})']
    
    # Merge the current environment with the extra environment
    env = os.environ.copy()
    env.update(extra_env)
    
    # Run the subprocess
    result = subprocess.run(command, env=env, timeout=timeout, capture_output=True, text=True)
    
    return result