import subprocess

def run_command(comandi, argomenti, cwd=None, verbose=False, nascondi_stderr=False, env=None):
    """
    Esegui il comando specificato.

    :param comandi: Lista di comandi da eseguire.
    :param argomenti: Lista di argomenti da passare ai comandi.
    :param cwd: Directory di lavoro corrente (opzionale).
    :param verbose: Se True, stampa l'output del comando (opzionale).
    :param nascondi_stderr: Se True, nasconde l'output di errore (opzionale).
    :param env: Dizionario di variabili d'ambiente (opzionale).
    :return: Il codice di ritorno del comando.
    """
    command = comandi + argomenti
    stderr = subprocess.DEVNULL if nascondi_stderr else subprocess.PIPE
    
    process = subprocess.Popen(
        command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=stderr,
        env=env,
        text=True
    )
    
    stdout, stderr = process.communicate()
    
    if verbose:
        print(stdout)
    
    return process.returncode