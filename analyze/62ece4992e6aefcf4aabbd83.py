def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    दिए गए कमांड(s) को कॉल करें।
    """
    import subprocess
    import sys
    
    if isinstance(commands, str):
        commands = [commands]
        
    if isinstance(args, str):
        args = [args]
        
    for cmd in commands:
        cmd_list = [cmd]
        cmd_list.extend(args)
        
        stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
        
        if verbose:
            print(f"Running command: {' '.join(cmd_list)}")
            
        try:
            process = subprocess.Popen(
                cmd_list,
                stdout=subprocess.PIPE,
                stderr=stderr,
                cwd=cwd,
                env=env,
                universal_newlines=True
            )
            
            stdout, stderr = process.communicate()
            
            if process.returncode != 0:
                if stderr and not hide_stderr:
                    print(f"Error: {stderr}", file=sys.stderr)
                return False
                
            if stdout and verbose:
                print(stdout)
                
        except Exception as e:
            if not hide_stderr:
                print(f"Error executing command: {e}", file=sys.stderr)
            return False
            
    return True