def subprocess_run_helper(func, *args, timeout, extra_env=None):
    import subprocess
    import sys
    import os
    
    # Get the module and function name
    module_name = func.__module__
    func_name = func.__name__
    
    # Build the command to run
    cmd = [sys.executable, '-c', 
           f'import {module_name}; {module_name}.{func_name}(*{args})']
    
    # Set up environment variables
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
        
    # Run the subprocess with timeout
    try:
        result = subprocess.run(cmd, 
                              env=env,
                              timeout=timeout,
                              check=True,
                              capture_output=True,
                              text=True)
        return result
    except subprocess.TimeoutExpired as e:
        raise TimeoutError(f"Function timed out after {timeout} seconds") from e
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Function failed with return code {e.returncode}") from e