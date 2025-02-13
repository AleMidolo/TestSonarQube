import subprocess
import sys
import os

def subprocess_run_helper(func, *args, timeout=None, extra_env=None):
    module_name = func.__module__
    function_name = func.__name__
    
    # Prepare the command to run
    command = [sys.executable, '-c', f'import {module_name}; {module_name}.{function_name}(*{args})']
    
    # Set up the environment
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
    
    # Run the subprocess
    result = subprocess.run(command, env=env, timeout=timeout)
    
    return result