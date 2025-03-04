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

    # Imposta stderr
    if nascondi_stderr:
        stderr = subprocess.DEVNULL
    else:
        stderr = subprocess.PIPE

    try:
        # Esegui il comando
        if verbose:
            print(f"Esecuzione comando: {' '.join(cmd)}")
            
        processo = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=stderr,
            cwd=cwd,
            env=env,
            universal_newlines=True
        )
        
        output, error = processo.communicate()
        
        if processo.returncode != 0:
            if error and not nascondi_stderr:
                print(f"Errore: {error}", file=sys.stderr)
            return False
            
        return output.strip() if output else True
        
    except Exception as e:
        if verbose:
            print(f"Errore nell'esecuzione del comando: {str(e)}", file=sys.stderr)
        return False