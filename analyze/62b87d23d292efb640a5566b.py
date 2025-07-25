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
            
            output = process.communicate()[0]
            retcode = process.poll()
            
            if retcode:
                raise subprocess.CalledProcessError(
                    retcode, cmd_list, output=output
                )
                
            return output.strip()
            
        except (OSError, subprocess.CalledProcessError) as e:
            if verbose:
                print('Error running command:', str(e))
            raise