import subprocess
import os
import sys
import multiprocessing

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
    def target():
        # Set up the environment
        if extra_env is not None:
            os.environ.update(extra_env)
        
        # Prepare the arguments for the function
        func_args = [func.__module__, func.__name__] + list(args)
        
        # Call the function
        return func(*args)

    # Create a subprocess
    process = multiprocessing.Process(target=target)
    process.start()
    
    # Wait for the process to complete or timeout
    process.join(timeout)
    
    if process.is_alive():
        process.terminate()
        process.join()
        raise TimeoutError("The function call timed out.")
    
    return process.exitcode