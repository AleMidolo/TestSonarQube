def get_config():
    """
    Create, populate and return the VersioneerConfig() object.
    """
    cfg = VersioneerConfig()
    cfg.VCS = "git"
    cfg.style = "pep440"
    cfg.tag_prefix = ""
    cfg.parentdir_prefix = "myproject-" 
    cfg.versionfile_source = "src/myproject/_version.py"
    cfg.verbose = False
    return cfg