import subprocess

def run_command(comandi, argomenti, cwd=None, verbose=False, nascondi_stderr=False, env=None):
    """
    Esegui il comando specificato.

    :param comandi: Lista di comandi da eseguire.
    :param argomenti: Lista di argomenti da passare ai comandi.
    :param cwd: Directory di lavoro corrente (opzionale).
    :param verbose: Se True, stampa il comando eseguito (opzionale).
    :param nascondi_stderr: Se True, nasconde l'output di stderr (opzionale).
    :param env: Dizionario delle variabili d'ambiente (opzionale).
    :return: Il risultato dell'esecuzione del comando.
    """
    command = comandi + argomenti
    if verbose:
        print(f"Esecuzione del comando: {' '.join(command)}")
    
    stderr = subprocess.DEVNULL if nascondi_stderr else subprocess.PIPE
    
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            env=env,
            stdout=subprocess.PIPE,
            stderr=stderr,
            text=True
        )
        if verbose:
            print(f"Output del comando: {result.stdout}")
        return result
    except subprocess.CalledProcessError as e:
        if verbose:
            print(f"Errore durante l'esecuzione del comando: {e}")
        raise