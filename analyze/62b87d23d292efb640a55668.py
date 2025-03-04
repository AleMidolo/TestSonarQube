def get_config():
    """
    Create, populate and return the VersioneerConfig() object.
    """
    cfg = VersioneerConfig()
    
    # Set default configuration values
    cfg.VCS = "git"
    cfg.style = "pep440"
    cfg.tag_prefix = ""
    cfg.parentdir_prefix = ""
    cfg.versionfile_source = "src/_version.py"
    cfg.verbose = False
    cfg.update_files = True
    cfg.git_describe_args = "tags"
    cfg.lookupfile = ".versioneer-lookup"
    cfg.versionfile_build = None
    cfg.tag_regex = r"^v[0-9]+\.[0-9]+\.[0-9]+$"
    cfg.parentdir_regex = r"^(?P<parent>.*?)-(?P<version>[^-]+)$"
    cfg.git_get_keywords = {}
    cfg.git_keywords = {}
    
    return cfg