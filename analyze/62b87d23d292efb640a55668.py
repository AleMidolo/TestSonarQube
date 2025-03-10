def get_config():
    """
    Create, populate and return the VersioneerConfig() object.
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = "0.1.0"
            self.tag_prefix = "v"
            self.parentdir_prefix = "myproject-"
            self.vcs = "git"
            self.style = "pep440"
            self.long_version = "0.1.0+0.g1234567"
            self.short_version = "0.1.0"
            self.error = None

    config = VersioneerConfig()
    return config