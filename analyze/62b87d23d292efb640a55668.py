def get_config():
    """
    Crea, popola e restituisci l'oggetto VersioneerConfig()
    """
    from versioneer import VersioneerConfig
    
    config = VersioneerConfig()
    
    # Populate config settings
    config.VCS = "git"
    config.style = "pep440"
    config.tag_prefix = ""
    config.parentdir_prefix = "myproject-"
    config.versionfile_source = "myproject/_version.py"
    config.verbose = False
    
    return config