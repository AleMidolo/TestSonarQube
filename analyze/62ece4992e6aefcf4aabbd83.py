def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Esegui il/i comando/i fornito/i.
    """
    import subprocess
    import shlex
    
    if isinstance(commands, str):
        commands = [commands]
        
    if isinstance(args, str):
        args = shlex.split(args)
    elif args is None:
        args = []
        
    for cmd in commands:
        full_cmd = [cmd] + args
        
        if verbose:
            print(f"Executing command: {' '.join(full_cmd)}")
            
        stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
            
        try:
            process = subprocess.Popen(
                full_cmd,
                stdout=subprocess.PIPE,
                stderr=stderr,
                cwd=cwd,
                env=env,
                universal_newlines=True
            )
            
            stdout, stderr = process.communicate()
            
            if process.returncode != 0:
                raise subprocess.CalledProcessError(
                    process.returncode, 
                    full_cmd,
                    stdout,
                    stderr
                )
                
            if verbose and stdout:
                print(stdout)
                
            return stdout.strip() if stdout else ""
            
        except (subprocess.CalledProcessError, OSError) as e:
            if verbose:
                print(f"Error executing command: {str(e)}")
            raise