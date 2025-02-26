import subprocess
import os
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
    def run_func(queue, *args):
        result = func(*args)
        queue.put(result)

    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=run_func, args=(queue, *args), env=extra_env)
    process.start()
    process.join(timeout)

    if process.is_alive():
        process.terminate()
        process.join()
        raise TimeoutError("The function call timed out.")

    return queue.get()