import subprocess
import os
import sys
import multiprocessing

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
    # Prepare the environment
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Create a new process to run the function
    def target():
        # Call the function with the provided arguments
        func(*args)

    # Create a process
    process = multiprocessing.Process(target=target)

    # Start the process
    process.start()

    # Wait for the process to complete or timeout
    process.join(timeout)

    # Check if the process is still alive
    if process.is_alive():
        process.terminate()
        process.join()
        raise TimeoutError("The function execution timed out.")

    return process.exitcode