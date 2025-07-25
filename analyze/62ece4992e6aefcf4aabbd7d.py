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
    import subprocess
    import os
    import sys
    
    # Get the module and function name
    module_name = func.__module__
    func_name = func.__name__
    
    # Build the command to run
    cmd = [sys.executable, "-c",
           f"from {module_name} import {func_name}; {func_name}()"]
    
    # Add any additional arguments
    cmd.extend(args)
    
    # Set up environment
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
        
    # Run the subprocess with timeout
    try:
        result = subprocess.run(
            cmd,
            env=env,
            timeout=timeout,
            check=True,
            capture_output=True,
            text=True
        )
        return result
    except subprocess.TimeoutExpired as e:
        raise TimeoutError(f"Function timed out after {timeout} seconds") from e
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Function failed with exit code {e.returncode}") from e