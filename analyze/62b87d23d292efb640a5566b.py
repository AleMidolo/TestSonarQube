import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Llama al/los comando(s) dado(s).

    :param commands: Lista de comandos a ejecutar.
    :param args: Lista de argumentos para los comandos.
    :param cwd: Directorio de trabajo actual (opcional).
    :param verbose: Si es True, muestra la salida del comando (opcional).
    :param hide_stderr: Si es True, oculta la salida de error (opcional).
    :param env: Diccionario de variables de entorno (opcional).
    :return: El resultado de la ejecución del comando.
    """
    command_list = commands + args
    stderr = subprocess.DEVNULL if hide_stderr else None
    stdout = subprocess.PIPE if verbose else None

    try:
        result = subprocess.run(
            command_list,
            cwd=cwd,
            env=env,
            stdout=stdout,
            stderr=stderr,
            text=True,
            check=True
        )
        if verbose:
            print(result.stdout)
        return result
    except subprocess.CalledProcessError as e:
        if verbose:
            print(f"Error: {e.stderr}")
        raise