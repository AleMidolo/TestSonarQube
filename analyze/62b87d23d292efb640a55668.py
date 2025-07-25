def get_config():
    """
    Create, populate and return the VersioneerConfig() object.
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = "0.1.0"
            self.vcs = "git"
            self.style = "pep440"
            self.tag_prefix = "v"
            self.parentdir_prefix = "myproject-"
            self.versionfile_source = "myproject/_version.py"
            self.verbose = False

        def __repr__(self):
            return f"VersioneerConfig(version={self.version}, vcs={self.vcs}, style={self.style}, tag_prefix={self.tag_prefix}, parentdir_prefix={self.parentdir_prefix}, versionfile_source={self.versionfile_source}, verbose={self.verbose})"

    config = VersioneerConfig()
    return config