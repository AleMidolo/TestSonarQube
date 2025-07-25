def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Call the given command(s).
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
                raise subprocess.CalledProcessError(process.returncode, cmd_list)
                
            if verbose and output:
                print(output)
                
            return output.strip() if output else ""
            
        except FileNotFoundError:
            print(f"Command not found: {cmd}", file=sys.stderr)
            raise
        except Exception as e:
            print(f"Error executing command: {e}", file=sys.stderr)
            raise