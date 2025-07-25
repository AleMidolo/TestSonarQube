def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    दिए गए कमांड(s) को चलाएं।
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
            print("Running command:", " ".join(cmd_list))
            
        try:
            stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
            process = subprocess.Popen(
                cmd_list,
                stdout=subprocess.PIPE,
                stderr=stderr,
                cwd=cwd,
                env=env,
                universal_newlines=True
            )
            
            output, error = process.communicate()
            
            if process.returncode != 0:
                if error and not hide_stderr:
                    print(f"Error: {error}", file=sys.stderr)
                return False
                
            if output and verbose:
                print(output)
                
        except Exception as e:
            if not hide_stderr:
                print(f"Error executing command: {e}", file=sys.stderr)
            return False
            
    return True