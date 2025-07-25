def get_config():
    """
    # VersioneerConfig() ऑब्जेक्ट बनाएं, इसे डेटा से भरें और इसे लौटाएं।
    """
    cfg = VersioneerConfig()
    
    cfg.VCS = "git"
    cfg.style = "pep440"
    cfg.tag_prefix = ""
    cfg.parentdir_prefix = "versioneer-"
    cfg.versionfile_source = "src/_version.py"
    cfg.verbose = False
    cfg.versionfile_build = None
    cfg.tag_regex = r"^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$"
    cfg.parentdir_regex = r"^(?P<prefix>.*?-)?(?P<version>[^\+]+)(?P<suffix>.*)?$"
    
    return cfg