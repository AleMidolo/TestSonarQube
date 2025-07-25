def get_config():
    """
    Crea, popola e restituisci l'oggetto VersioneerConfig()
    """
    from versioneer import get_config as get_versioneer_config
    config = get_versioneer_config()
    return config