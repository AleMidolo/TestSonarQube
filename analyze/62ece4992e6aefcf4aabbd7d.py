import subprocess
import os
import sys

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
    # Asegurarse de que el módulo de la función esté en el sys.path
    module_name = func.__module__
    if module_name not in sys.modules:
        __import__(module_name)

    # Crear el entorno para el subproceso
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Preparar el comando a ejecutar
    command = [sys.executable, '-c', f'import {module_name}; {func.__name__}(*{args})']

    # Ejecutar el subproceso
    result = subprocess.run(command, env=env, timeout=timeout, capture_output=True, text=True)

    return result