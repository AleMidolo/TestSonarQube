def subprocess_run_helper(func, *args, timeout, extra_env=None):
    import subprocess
    import sys
    import os
    
    # Prepare environment variables
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
        
    # Get function module and name
    module_name = func.__module__
    func_name = func.__name__
    
    # Build Python command to execute function
    cmd = [
        sys.executable,
        '-c',
        f'import {module_name}; {module_name}.{func_name}()'
    ]
    
    # Add any additional command line arguments
    if args:
        cmd.extend(args)
        
    # Run subprocess with timeout
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
        print(f"Process timed out after {timeout} seconds")
        raise e
    except subprocess.CalledProcessError as e:
        print(f"Process failed with return code {e.returncode}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        raise e