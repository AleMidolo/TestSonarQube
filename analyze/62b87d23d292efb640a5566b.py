import subprocess
import os

def run_command(comandi, argomenti, cwd=None, verbose=False, nascondi_stderr=False, env=None):
    """
    Esegui il comando specificato.
    """
    if cwd is None:
        cwd = os.getcwd()
    
    if env is None:
        env = os.environ

    command = [comandi] + argomenti
    stderr = subprocess.DEVNULL if nascondi_stderr else None

    if verbose:
        print(f"Esecuzione comando: {' '.join(command)} in {cwd}")

    result = subprocess.run(command, cwd=cwd, env=env, stderr=stderr)

    return result.returncode