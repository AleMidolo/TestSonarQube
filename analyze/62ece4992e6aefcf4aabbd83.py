def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Esegui il/i comando/i fornito/i.
    """
    import subprocess
    import shlex
    
    # Handle single command or list of commands
    if isinstance(commands, str):
        commands = [commands]
        
    # Handle single arg or list of args
    if isinstance(args, str):
        args = [args]
    elif args is None:
        args = []
        
    results = []
    
    for cmd in commands:
        # Build full command with arguments
        full_cmd = shlex.split(cmd) + args
        
        # Configure subprocess options
        stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
        
        # Print command if verbose
        if verbose:
            print(f"Executing: {' '.join(full_cmd)}")
            
        try:
            # Run command
            process = subprocess.Popen(
                full_cmd,
                stdout=subprocess.PIPE,
                stderr=stderr,
                cwd=cwd,
                env=env,
                universal_newlines=True
            )
            
            # Get output
            stdout, stderr = process.communicate()
            
            # Store results
            result = {
                'command': cmd,
                'returncode': process.returncode,
                'stdout': stdout.strip() if stdout else '',
                'stderr': stderr.strip() if stderr else ''
            }
            
            results.append(result)
            
            if verbose:
                print(f"Return code: {result['returncode']}")
                if stdout:
                    print(f"Output:\n{result['stdout']}")
                if stderr and not hide_stderr:
                    print(f"Error:\n{result['stderr']}")
                    
        except Exception as e:
            if verbose:
                print(f"Error executing {cmd}: {str(e)}")
            results.append({
                'command': cmd,
                'returncode': -1,
                'stdout': '',
                'stderr': str(e)
            })
            
    return results[0] if len(results) == 1 else results