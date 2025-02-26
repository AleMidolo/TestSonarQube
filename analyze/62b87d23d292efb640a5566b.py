import subprocess
import os

def run_command(comandi, argomenti, cwd=None, verbose=False, nascondi_stderr=False, env=None):
    """
    Esegui il comando specificato.
    """
    if cwd is None:
        cwd = os.getcwd()
    
    full_command = [comandi] + argomenti
    stderr_option = subprocess.DEVNULL if nascondi_stderr else None
    
    if verbose:
        print(f"Esecuzione comando: {' '.join(full_command)} in {cwd}")
    
    result = subprocess.run(full_command, cwd=cwd, env=env, stderr=stderr_option)
    
    return result.returncode