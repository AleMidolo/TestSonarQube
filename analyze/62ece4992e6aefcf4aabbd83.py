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
        
        if verbose:
            print(f"Running command: {' '.join(cmd_list)}")
            
        try:
            stderr = subprocess.DEVNULL if hide_stderr else None
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
                if not hide_stderr and error:
                    sys.stderr.write(error)
                raise subprocess.CalledProcessError(process.returncode, cmd)
                
            if verbose and output:
                print(output)
                
            return output.strip() if output else ""
            
        except (OSError, subprocess.CalledProcessError) as e:
            if verbose:
                print(f"Command failed: {str(e)}")
            raise