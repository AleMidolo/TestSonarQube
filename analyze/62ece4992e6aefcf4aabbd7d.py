import subprocess
import sys
import os
import importlib

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
    module_name = func.__module__
    func_name = func.__name__

    # Prepare the environment
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Prepare the command to run the function in a subprocess
    command = [
        sys.executable,
        "-c",
        f"from {module_name} import {func_name}; {func_name}(*{args})"
    ]

    # Run the subprocess
    result = subprocess.run(command, env=env, timeout=timeout, check=True)

    return result