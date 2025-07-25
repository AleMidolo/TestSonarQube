import subprocess

def run_command(comandi, argomenti, cwd=None, verbose=False, nascondi_stderr=False, env=None):
    """
    Esegui il comando specificato.

    :param comandi: Lista di comandi da eseguire.
    :param argomenti: Lista di argomenti da passare ai comandi.
    :param cwd: Directory di lavoro corrente (opzionale).
    :param verbose: Se True, stampa il comando eseguito (opzionale).
    :param nascondi_stderr: Se True, nasconde l'output di stderr (opzionale).
    :param env: Dizionario di variabili d'ambiente (opzionale).
    :return: Il risultato del comando eseguito.
    """
    command = comandi + argomenti
    stderr = subprocess.DEVNULL if nascondi_stderr else subprocess.PIPE
    
    if verbose:
        print(f"Esecuzione del comando: {' '.join(command)}")
    
    result = subprocess.run(
        command,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=stderr,
        text=True
    )
    
    if verbose:
        print(f"Output del comando:\n{result.stdout}")
        if result.stderr and not nascondi_stderr:
            print(f"Errore del comando:\n{result.stderr}")
    
    return result