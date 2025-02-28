def get_versions():
    """
    Ottieni le informazioni sulla versione o restituisci il valore predefinito se non è possibile ottenerle.
    """
    import sys
    import platform
    import subprocess

    try:
        # Ottieni la versione di Python
        python_version = sys.version.split()[0]

        # Ottieni la versione del sistema operativo
        os_version = platform.platform()

        # Ottieni la versione di pip (se disponibile)
        try:
            pip_version = subprocess.check_output([sys.executable, '-m', 'pip', '--version']).decode().split()[1]
        except Exception:
            pip_version = "N/A"

        return {
            "python_version": python_version,
            "os_version": os_version,
            "pip_version": pip_version
        }
    except Exception:
        return {
            "python_version": "N/A",
            "os_version": "N/A",
            "pip_version": "N/A"
        }