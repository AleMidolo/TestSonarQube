import subprocess

def run_command(commands, args, cwd=None, verbose=False, hide_stderr=False, env=None):
    """
    Llama al/los comando(s) dado(s).
    
    :param commands: Lista de comandos a ejecutar.
    :param args: Lista de argumentos para los comandos.
    :param cwd: Directorio de trabajo actual (opcional).
    :param verbose: Si es True, imprime el comando ejecutado (opcional).
    :param hide_stderr: Si es True, oculta la salida de error estándar (opcional).
    :param env: Diccionario de variables de entorno (opcional).
    :return: El código de retorno del comando ejecutado.
    """
    full_command = commands + args
    if verbose:
        print(f"Ejecutando: {' '.join(full_command)}")
    
    stderr = subprocess.DEVNULL if hide_stderr else None
    
    process = subprocess.Popen(
        full_command,
        cwd=cwd,
        env=env,
        stderr=stderr
    )
    
    process.communicate()
    return process.returncode