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
    :return: Il risultato dell'esecuzione del comando.
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
        print(f"Output del comando: {result.stdout}")
        if result.stderr:
            print(f"Errore del comando: {result.stderr}")
    
    return result