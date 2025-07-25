def get_config():
    """
    Crea, popola e restituisci l'oggetto VersioneerConfig()
    """
    from versioneer import VersioneerConfig

    config = VersioneerConfig()
    # Populate the config object with necessary data
    # Example:
    # config.VCS = "git"
    # config.style = "pep440"
    # config.versionfile_source = "myproject/_version.py"
    # config.tag_prefix = "v"
    
    return config