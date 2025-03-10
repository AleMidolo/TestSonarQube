def get_config():
    """
    Crea, popola e restituisci l'oggetto VersioneerConfig()
    """
    from versioneer import VersioneerConfig

    config = VersioneerConfig()
    # Populate the config object with necessary attributes
    config.VCS = "git"
    config.style = "pep440"
    config.versionfile_source = "my_package/_version.py"
    config.versionfile_build = "my_package/_version.py"
    config.tag_prefix = "v"
    config.parentdir_prefix = "my_package-"

    return config