import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Llama al/los comando(s) dado(s).

    :param commands: Lista de comandos a ejecutar.
    :param args: Lista de argumentos para los comandos.
    :param cwd: Directorio de trabajo actual (opcional).
    :param verbose: Si es True, imprime la salida del comando (opcional).
    :param hide_stderr: Si es True, oculta la salida de error (opcional).
    :param env: Diccionario de variables de entorno (opcional).
    :return: Tupla con el código de salida y la salida del comando.
    """
    full_command = commands + args
    stderr = subprocess.PIPE if hide_stderr else None
    
    process = subprocess.Popen(
        full_command,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=stderr,
        env=env,
        text=True
    )
    
    stdout, stderr = process.communicate()
    
    if verbose:
        print(stdout)
    
    return process.returncode, stdout