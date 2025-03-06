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
    :return: El código de retorno del comando.
    """
    command = commands + args
    stderr = subprocess.DEVNULL if hide_stderr else None
    stdout = None if verbose else subprocess.DEVNULL

    process = subprocess.Popen(
        command,
        cwd=cwd,
        stdout=stdout,
        stderr=stderr,
        env=env
    )
    process.communicate()
    return process.returncode