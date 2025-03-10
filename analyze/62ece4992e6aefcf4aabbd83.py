import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Esegui il/i comando/i fornito/i.
    
    :param commands: Lista di comandi da eseguire.
    :param args: Lista di argomenti da passare ai comandi.
    :param cwd: Directory di lavoro corrente (opzionale).
    :param verbose: Se True, stampa i comandi eseguiti (opzionale).
    :param hide_stderr: Se True, nasconde l'output di stderr (opzionale).
    :param env: Dizionario di variabili d'ambiente (opzionale).
    :return: Il codice di ritorno del comando eseguito.
    """
    full_command = commands + args
    if verbose:
        print(f"Esecuzione del comando: {' '.join(full_command)}")
    
    stderr = subprocess.DEVNULL if hide_stderr else None
    
    process = subprocess.Popen(
        full_command,
        cwd=cwd,
        env=env,
        stdout=subprocess.PIPE,
        stderr=stderr
    )
    
    stdout, _ = process.communicate()
    
    if verbose:
        print(stdout.decode())
    
    return process.returncode