import subprocess
import sys
import os
import pickle

def subprocess_run_helper(func, *args, timeout, extra_env=None):
    # Serialize the function and its arguments
    func_data = pickle.dumps((func, args))
    
    # Create a new environment for the subprocess
    env = os.environ.copy()
    if extra_env is not None:
        env.update(extra_env)
    
    # Run the subprocess
    result = subprocess.run(
        [sys.executable, "-c", 
         f"import pickle; func, args = pickle.loads({func_data}); func(*args)"],
        env=env,
        timeout=timeout,
        capture_output=True,
        text=True
    )
    
    # Return the result
    return result