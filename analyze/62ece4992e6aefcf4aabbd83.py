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
    :return: Il codice di ritorno del comando eseguito.
    """
    command = commands + args
    stderr = subprocess.DEVNULL if hide_stderr else None
    process = subprocess.Popen(
        command,
        cwd=cwd,
        stdout=subprocess.PIPE if verbose else None,
        stderr=stderr,
        env=env
    )
    stdout, _ = process.communicate()
    if verbose and stdout:
        print(stdout.decode())
    return process.returncode