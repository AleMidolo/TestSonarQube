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

        # Obtener la versión de Git si está instalado
        try:
            git_version = subprocess.check_output(['git', '--version']).decode().strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            git_version = "Git no está instalado o no se pudo obtener la versión."

        return {
            "python_version": python_version,
            "os_version": os_version,
            "git_version": git_version
        }
    except Exception as e:
        # En caso de error, devolver un valor predeterminado
        return {
            "python_version": "Desconocido",
            "os_version": "Desconocido",
            "git_version": "Desconocido"
        }