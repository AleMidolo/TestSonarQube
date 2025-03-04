def run_command(comandi, argomenti, cwd=None, verbose=False, nascondi_stderr=False, env=None):
    """
    Esegui il comando specificato.
    """
    import subprocess
    import sys

    # Costruisci il comando completo
    if isinstance(comandi, str):
        cmd = [comandi]
    else:
        cmd = list(comandi)
        
    if argomenti:
        if isinstance(argomenti, str):
            cmd.append(argomenti)
        else:
            cmd.extend(argomenti)

    # Imposta gli stream di output
    stdout = subprocess.PIPE
    stderr = subprocess.DEVNULL if nascondi_stderr else subprocess.PIPE

    try:
        # Esegui il comando
        process = subprocess.Popen(
            cmd,
            stdout=stdout,
            stderr=stderr,
            cwd=cwd,
            env=env
        )

        # Leggi l'output
        out, err = process.communicate()
        
        # Decodifica l'output
        if out:
            out = out.decode('utf-8')
        if err:
            err = err.decode('utf-8')

        # Stampa l'output se verbose è True
        if verbose:
            if out:
                print(out)
            if err and not nascondi_stderr:
                print(err, file=sys.stderr)

        # Restituisci il codice di uscita, l'output e l'errore
        return process.returncode, out, err

    except Exception as e:
        if verbose:
            print(f"Errore nell'esecuzione del comando: {e}", file=sys.stderr)
        return -1, None, str(e)