def subprocess_run_helper(func, *args, timeout, extra_env=None):
    import subprocess
    import sys
    import os
    from inspect import getmodule

    # Get the module name and function name
    module_name = getmodule(func).__name__
    func_name = func.__name__

    # Build command to run in subprocess
    cmd = [sys.executable, '-c',
           f'import {module_name}; {module_name}.{func_name}()']
    
    # Add any additional arguments
    cmd.extend(args)

    # Set up environment
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Run the subprocess
    result = subprocess.run(
        cmd,
        env=env,
        timeout=timeout,
        capture_output=True,
        text=True
    )

    return result