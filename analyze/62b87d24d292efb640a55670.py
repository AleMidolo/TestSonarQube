def get_versions():
    """
    Obtén la información de la versión o devuelve el valor predeterminado si no es posible obtenerla.
    """
    import sys
    import platform
    import subprocess

    try:
        # Obtener la versión de Python
        python_version = sys.version.split()[0]

        # Obtener la versión del sistema operativo
        os_version = platform.platform()

        # Obtener la versión de pip (si está instalado)
        try:
            pip_version = subprocess.check_output([sys.executable, '-m', 'pip', '--version']).decode().split()[1]
        except Exception:
            pip_version = "No disponible"

        return {
            "python_version": python_version,
            "os_version": os_version,
            "pip_version": pip_version
        }
    except Exception as e:
        # En caso de error, devolver un valor predeterminado
        return {
            "python_version": "No disponible",
            "os_version": "No disponible",
            "pip_version": "No disponible"
        }