import subprocess
import sys
import os

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
    # Crear un entorno modificado si se proporciona extra_env
    env = os.environ.copy()
    if extra_env is not None:
        env.update(extra_env)

    # Construir el comando para ejecutar la función en un subproceso
    module_name = func.__module__
    func_name = func.__name__
    command = [sys.executable, '-c', f'from {module_name} import {func_name}; {func_name}()']

    # Agregar argumentos adicionales si los hay
    if args:
        command.extend(args)

    # Ejecutar el comando en un subproceso
    result = subprocess.run(command, env=env, timeout=timeout, capture_output=True, text=True)

    # Devolver el resultado del subproceso
    return result