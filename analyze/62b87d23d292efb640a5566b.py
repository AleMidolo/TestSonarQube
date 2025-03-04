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
            env=env,
            universal_newlines=True
        )

        # Leggi l'output
        out, err = process.communicate()
        
        # Stampa l'output se verbose è True
        if verbose:
            if out:
                print(out)
            if err and not nascondi_stderr:
                print(err, file=sys.stderr)

        return process.returncode, out, err

    except Exception as e:
        if verbose:
            print(f"Errore nell'esecuzione del comando: {e}", file=sys.stderr)
        return -1, "", str(e)