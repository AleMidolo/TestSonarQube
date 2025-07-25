def get_config():
    """
    Crea, completa y devuelve el objeto VersioneerConfig().
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = None
            self.tag_prefix = None
            self.vcs = None

        def set_version(self, version):
            self.version = version

        def set_tag_prefix(self, tag_prefix):
            self.tag_prefix = tag_prefix

        def set_vcs(self, vcs):
            self.vcs = vcs

    config = VersioneerConfig()
    config.set_version("0.1.0")
    config.set_tag_prefix("v")
    config.set_vcs("git")

    return config