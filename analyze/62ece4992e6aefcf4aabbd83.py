def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Llama al/los comando(s) dado(s).
    """
    import subprocess
    import sys
    
    if isinstance(commands, str):
        commands = [commands]
        
    for cmd in commands:
        cmd_list = [cmd]
        if args:
            if isinstance(args, str):
                cmd_list.append(args)
            else:
                cmd_list.extend(args)
                
        if verbose:
            print("Running command: " + " ".join(cmd_list))
            
        stderr = subprocess.DEVNULL if hide_stderr else None
            
        try:
            subprocess.check_call(cmd_list, cwd=cwd, stderr=stderr, env=env)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code {e.returncode}")
            sys.exit(1)
        except FileNotFoundError:
            print(f"Command not found: {cmd}")
            sys.exit(1)