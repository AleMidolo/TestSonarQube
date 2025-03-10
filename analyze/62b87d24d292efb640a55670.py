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

        # Obtener la versión de setuptools (si está instalado)
        try:
            setuptools_version = subprocess.check_output([sys.executable, '-m', 'pip', 'show', 'setuptools']).decode().split('\n')[1].split()[1]
        except Exception:
            setuptools_version = "No disponible"

        return {
            "Python": python_version,
            "Sistema Operativo": os_version,
            "Pip": pip_version,
            "Setuptools": setuptools_version
        }

    except Exception as e:
        # En caso de error, devolver un valor predeterminado
        return {
            "Python": "No disponible",
            "Sistema Operativo": "No disponible",
            "Pip": "No disponible",
            "Setuptools": "No disponible"
        }