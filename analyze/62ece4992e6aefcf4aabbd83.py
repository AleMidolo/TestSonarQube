import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Esegui il/i comando/i fornito/i.
    
    :param commands: Lista di comandi da eseguire.
    :param args: Lista di argomenti da passare ai comandi.
    :param cwd: Directory di lavoro corrente (opzionale).
    :param verbose: Se True, stampa l'output del comando (opzionale).
    :param hide_stderr: Se True, nasconde l'output di errore (opzionale).
    :param env: Dizionario di variabili d'ambiente (opzionale).
    :return: Il codice di ritorno del comando.
    """
    full_command = commands + args
    stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
    
    process = subprocess.Popen(
        full_command,
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