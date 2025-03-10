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
    :return: Tupla con el código de salida y la salida del comando.
    """
    command = commands + args
    stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
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
        if stderr and not hide_stderr:
            print(stderr)
    
    return process.returncode, stdout