def get_config():
    """
    返回一个新的 `VersioneerConfig()` 对象，并设置其各种属性。
    创建、填充并返回 `VersioneerConfig()` 对象。
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = None
            self.tag_prefix = None
            self.parentdir_prefix = None
            self.vcs = None
            self.style = None
            self.long_version_py = None
            self.short_version_py = None
            self.verbose = False

    config = VersioneerConfig()
    config.version = "0.1"
    config.tag_prefix = "v"
    config.parentdir_prefix = "project-"
    config.vcs = "git"
    config.style = "pep440"
    config.long_version_py = "long_version.py"
    config.short_version_py = "short_version.py"
    config.verbose = True

    return config