import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Llama al/los comando(s) dado(s).

    :param commands: Lista de comandos a ejecutar.
    :param args: Lista de argumentos para los comandos.
    :param cwd: Directorio de trabajo actual (opcional).
    :param verbose: Si es True, muestra la salida del comando (opcional).
    :param hide_stderr: Si es True, oculta los errores (opcional).
    :param env: Diccionario de variables de entorno (opcional).
    :return: El resultado de la ejecución del comando.
    """
    if not isinstance(commands, list):
        commands = [commands]
    
    if not isinstance(args, list):
        args = [args]
    
    full_command = commands + args
    
    stderr = subprocess.DEVNULL if hide_stderr else subprocess.PIPE
    
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
    
    if process.returncode != 0 and not hide_stderr:
        print(f"Error: {stderr}")
    
    return stdout