def subprocess_run_helper(func, *args, timeout, extra_env=None):
    import subprocess
    import sys
    import os
    from importlib import util

    # Obtener el módulo y nombre de la función
    module_name = func.__module__
    func_name = func.__name__

    # Preparar el entorno
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)

    # Construir el comando Python para ejecutar la función
    cmd = [
        sys.executable,
        '-c',
        f'import {module_name}; {module_name}.{func_name}()'
    ]

    # Agregar argumentos adicionales
    if args:
        cmd.extend(args)

    try:
        # Ejecutar el subproceso
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
        raise TimeoutError(f"La función {func_name} excedió el tiempo límite de {timeout} segundos")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error al ejecutar {func_name}: {e.stderr}")