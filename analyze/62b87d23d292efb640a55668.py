def get_config():
    """
    Create, populate and return the VersioneerConfig() object.
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = "0.1.0"
            self.vcs = "git"
            self.tag_prefix = "v"
            self.parentdir_prefix = ""

    config = VersioneerConfig()
    return config