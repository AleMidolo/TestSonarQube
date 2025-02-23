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
    # Asegurarse de que el módulo que contiene la función está en el path
    module_name = func.__module__
    if module_name not in sys.modules:
        __import__(module_name)

    # Preparar el entorno
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Ejecutar la función en un subproceso
    result = subprocess.run(
        [sys.executable, '-c', f'import {module_name}; {module_name}.{func.__name__}(*{args})'],
        env=env,
        timeout=timeout,
        capture_output=True,
        text=True
    )

    return result