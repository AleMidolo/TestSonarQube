import subprocess
import sys
import os

def subprocess_run_helper(func, *args, timeout, extra_env=None):
    """
    Ejecutar una función en un subproceso.

    Parametros
    ----------
    func : funcion
        La función que se ejecutará. Debe estar en un módulo que sea importable.
    *args : str
        Cualquier argumento adicional de línea de comandos que se pasará como primer argumento a ``subprocess.run``.
    extra_env : dict[str, str]
        Cualquier variable de entorno adicional que se establecerá para el subproceso.
    """
    # Obtener el nombre del módulo y la función
    module_name = func.__module__
    func_name = func.__name__

    # Crear el comando para ejecutar la función
    command = [sys.executable, '-c', f'from {module_name} import {func_name}; {func_name}()']

    # Agregar argumentos adicionales si los hay
    if args:
        command.extend(args)

    # Combinar el entorno actual con el entorno adicional si se proporciona
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Ejecutar el subproceso
    result = subprocess.run(command, env=env, timeout=timeout, capture_output=True, text=True)

    # Devolver el resultado del subproceso
    return result