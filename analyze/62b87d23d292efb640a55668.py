def get_config():
    """
    Create, populate and return the VersioneerConfig() object.
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = "0.1.0"
            self.tag_prefix = "v"
            self.parentdir_prefix = "project-"
            self.vcs = "git"
            self.style = "pep440"
            self.long_version = "0.1.0+0.g0000000"
            self.short_version = "0.1.0"
            self.error = None

    config = VersioneerConfig()
    return config