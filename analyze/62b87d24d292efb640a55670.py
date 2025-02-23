def get_versions():
    """
    Ottieni le informazioni sulla versione o restituisci il valore predefinito se non è possibile ottenerle.
    """
    import platform

    try:
        version_info = {
            "python_version": platform.python_version(),
            "platform": platform.platform(),
            "system": platform.system(),
            "release": platform.release(),
        }
        return version_info
    except Exception:
        return "Version information could not be retrieved."