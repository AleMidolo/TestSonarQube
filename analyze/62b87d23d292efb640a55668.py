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
            self.long_version = False
            self.dirty = False

        def __repr__(self):
            return (f"VersioneerConfig(version={self.version}, tag_prefix={self.tag_prefix}, "
                    f"parentdir_prefix={self.parentdir_prefix}, vcs={self.vcs}, style={self.style}, "
                    f"long_version={self.long_version}, dirty={self.dirty})")

    config = VersioneerConfig()
    return config