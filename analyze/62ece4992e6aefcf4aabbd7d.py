import subprocess
import sys
import os
import pickle

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
    # Serialize the function and its arguments
    func_data = pickle.dumps((func, args))
    
    # Prepare the environment
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
    
    # Run the subprocess
    result = subprocess.run(
        [sys.executable, "-c", 
         "import pickle, sys; func, args = pickle.loads(sys.stdin.buffer.read()); func(*args)"],
        input=func_data,
        env=env,
        timeout=timeout,
        capture_output=True,
        text=True
    )
    
    # Check for errors
    if result.returncode != 0:
        raise RuntimeError(f"Subprocess failed with return code {result.returncode}: {result.stderr}")
    
    return result.stdout