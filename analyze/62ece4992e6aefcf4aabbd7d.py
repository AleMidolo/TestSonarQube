import subprocess
import sys
import os

def subprocess_run_helper(func, *args, timeout, extra_env=None):
    """
    Esegui una funzione in un sottoprocesso.

    Parametri
    ----------
    func : function
        La funzione da eseguire. Deve trovarsi in un modulo importabile.
    *args : str
        Eventuali argomenti aggiuntivi da riga di comando da passare
        come primo argomento a ``subprocess.run``.
    extra_env : dict[str, str]
        Eventuali variabili d'ambiente aggiuntive da impostare per il sottoprocesso.
    """
    # Ottieni il modulo e il nome della funzione
    module_name = func.__module__
    func_name = func.__name__

    # Costruisci il comando da eseguire
    command = [sys.executable, '-c', f'from {module_name} import {func_name}; {func_name}()']

    # Aggiungi eventuali argomenti aggiuntivi
    if args:
        command.extend(args)

    # Prepara l'ambiente
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Esegui il sottoprocesso
    result = subprocess.run(command, env=env, timeout=timeout, capture_output=True, text=True)

    return result