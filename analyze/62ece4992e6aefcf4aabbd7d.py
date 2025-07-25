import subprocess
import sys
import os
import inspect

def subprocess_run_helper(func, *args, timeout, extra_env=None):
    """
    Run a function in a sub-process.

    Parameters
    ----------
    func : function
        The function to be run.  It must be in a module that is importable.
    *args : str
        Any additional command line arguments to be passed in
        the first argument to ``subprocess.run``.
    extra_env : dict[str, str]
        Any additional environment variables to be set for the subprocess.
    """
    # Get the module and function name
    module_name = inspect.getmodule(func).__name__
    func_name = func.__name__

    # Prepare the command to run the function
    command = [sys.executable, '-c', f'from {module_name} import {func_name}; {func_name}()']

    # Add any additional arguments
    command.extend(args)

    # Prepare the environment
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Run the subprocess
    result = subprocess.run(command, env=env, timeout=timeout, capture_output=True, text=True)

    # Return the result
    return result