import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    if isinstance(commands, str):
        commands = [commands]
    
    results = []
    
    for command in commands:
        full_command = [command] + args
        if verbose:
            print(f"Running command: {' '.join(full_command)}")
        
        process = subprocess.Popen(full_command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE if not hide_stderr else subprocess.DEVNULL, env=env)
        stdout, stderr = process.communicate()
        returncode = process.returncode
        
        results.append((stdout.decode('utf-8'), returncode))
    
    return results