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
            print('Running:', ' '.join(cmd_list))
            
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
                print(f"Error executing command: {' '.join(cmd_list)}")
                if error and not hide_stderr:
                    print(f"Error output: {error}")
                sys.exit(process.returncode)
                
            if verbose and output:
                print(output)
                
            return output.strip() if output else None
            
        except Exception as e:
            print(f"Exception occurred while executing command: {' '.join(cmd_list)}")
            print(f"Error: {str(e)}")
            sys.exit(1)