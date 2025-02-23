import subprocess
import os
import sys

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
    # Creare un ambiente per il sottoprocesso
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Costruire il comando da eseguire
    command = [sys.executable, '-c', f'import {func.__module__}; {func.__module__}.{func.__name__}(*{args})']

    # Eseguire il comando nel sottoprocesso
    result = subprocess.run(command, env=env, timeout=timeout, capture_output=True, text=True)

    return result