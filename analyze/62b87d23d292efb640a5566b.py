import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Llama al/los comando(s) dado(s).

    :param commands: Lista de comandos a ejecutar.
    :param args: Lista de argumentos para los comandos.
    :param cwd: Directorio de trabajo actual (opcional).
    :param verbose: Si es True, muestra la salida del comando (opcional).
    :param hide_stderr: Si es True, oculta los errores estándar (opcional).
    :param env: Diccionario de variables de entorno (opcional).
    :return: El resultado de la ejecución del comando.
    """
    command = commands + args
    stderr = subprocess.PIPE if hide_stderr else None
    process = subprocess.Popen(
        command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=stderr,
        env=env,
        text=True
    )
    stdout, stderr = process.communicate()
    
    if verbose:
        print(stdout)
    
    if process.returncode != 0:
        if not hide_stderr and stderr:
            print(stderr)
        raise subprocess.CalledProcessError(process.returncode, command)
    
    return stdout