def subprocess_run_helper(func, *args, timeout, extra_env=None):
    import subprocess
    import sys
    import os
    from importlib import util

    # Obtener el módulo y nombre de la función
    module_name = func.__module__
    func_name = func.__name__

    # Construir el comando Python para ejecutar la función
    cmd = [sys.executable, '-c',
           f'import {module_name}; {module_name}.{func_name}()']
    
    # Agregar argumentos adicionales
    cmd.extend(args)

    # Preparar el entorno
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Ejecutar el subproceso
    try:
        result = subprocess.run(
            cmd,
            env=env,
            timeout=timeout,
            check=True,
            capture_output=True,
            text=True
        )
        return result
    except subprocess.TimeoutExpired as e:
        print(f"El proceso excedió el tiempo límite de {timeout} segundos")
        raise e
    except subprocess.CalledProcessError as e:
        print(f"El proceso falló con código de salida {e.returncode}")
        print(f"Salida de error: {e.stderr}")
        raise e