def get_config():
    """
    Crea, popola e restituisci l'oggetto VersioneerConfig()
    """
    from versioneer import get_config as versioneer_get_config
    config = versioneer_get_config()
    return config