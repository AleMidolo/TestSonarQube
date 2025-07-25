def get_config():
    """
    Crea, completa y devuelve el objeto VersioneerConfig().
    """
    from versioneer import VersioneerConfig
    
    config = VersioneerConfig()
    
    config.VCS = "git"
    config.style = "pep440"
    config.tag_prefix = ""
    config.parentdir_prefix = "myproject-"
    config.versionfile_source = "myproject/_version.py"
    config.verbose = False
    
    return config