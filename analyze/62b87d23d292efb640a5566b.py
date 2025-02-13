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

    stderr = subprocess.DEVNULL if nascondi_stderr else None

    process = subprocess.Popen(
        [comandi] + argomenti,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=stderr
    )

    if verbose:
        print(f"Esecuzione comando: {comandi} {' '.join(argomenti)} in {cwd}")

    stdout, _ = process.communicate()

    if process.returncode != 0:
        raise subprocess.CalledProcessError(process.returncode, comandi)

    return stdout.decode('utf-8').strip()