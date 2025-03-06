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
            self.long_version = "0.1.0+0.g1234567"
            self.short_version = "0.1.0"
            self.error = None

        def __repr__(self):
            return f"VersioneerConfig(version={self.version}, tag_prefix={self.tag_prefix}, parentdir_prefix={self.parentdir_prefix}, vcs={self.vcs}, style={self.style}, long_version={self.long_version}, short_version={self.short_version}, error={self.error})"

    config = VersioneerConfig()
    return config