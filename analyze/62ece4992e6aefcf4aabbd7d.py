def subprocess_run_helper(func, *args, timeout, extra_env=None):
    """
    Ejecutar una función en un subproceso.

    Parametros
    ----------
    func : funcion
        La función que se ejecutara. Debe estar en un modulo que sea importable.
    *args : str
        Cualquier argumento adicional de linea de comandos que se pasara como primer argumento a ``subprocess.run``.
    extra_env : dict[str, str]
        Cualquier variable de entorno adicional que se establecerá para el subproceso.
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