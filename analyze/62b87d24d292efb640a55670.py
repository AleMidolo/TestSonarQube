def get_versions():
    """
    Obtén la información de la versión o devuelve el valor predeterminado si no es posible obtenerla.
    """
    import sys
    import platform

    try:
        python_version = sys.version
        system_info = platform.system()
        system_version = platform.version()
        return {
            "python_version": python_version,
            "system_info": system_info,
            "system_version": system_version
        }
    except Exception as e:
        return {
            "python_version": "Unknown",
            "system_info": "Unknown",
            "system_version": "Unknown"
        }