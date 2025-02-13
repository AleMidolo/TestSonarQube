class VersioneerConfig:
    def __init__(self):
        self.version = None
        self.tag_prefix = None
        self.vcs = None
        self.versionfile_source = None
        self.versionfile_build = None

def get_config():
    config = VersioneerConfig()
    config.version = "0.1.0"
    config.tag_prefix = "v"
    config.vcs = "git"
    config.versionfile_source = "version.txt"
    config.versionfile_build = "build_version.txt"
    return config