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
    import subprocess
    import os

    # Prepare the environment
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Prepare the command
    command = [func.__module__ + '.' + func.__name__] + list(args)

    # Run the subprocess
    result = subprocess.run(command, env=env, timeout=timeout)

    return result