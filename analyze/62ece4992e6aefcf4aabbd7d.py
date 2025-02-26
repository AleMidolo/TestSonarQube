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
        if extra_env:
            os.environ.update(extra_env)
        # Call the function with the provided arguments
        return func(*args)

    # Create a process
    process = multiprocessing.Process(target=target)
    process.start()
    process.join(timeout)

    if process.is_alive():
        process.terminate()
        process.join()
        raise TimeoutError("The function call timed out.")

    return process.exitcode