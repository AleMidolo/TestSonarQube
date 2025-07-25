def get_versions():
    """
    Ottieni le informazioni sulla versione o restituisci il valore predefinito se non è possibile ottenerle.
    """
    import sys
    import platform

    try:
        python_version = sys.version
        os_info = platform.platform()
        return {
            "python_version": python_version,
            "os_info": os_info
        }
    except Exception as e:
        return {
            "python_version": "Unknown",
            "os_info": "Unknown"
        }