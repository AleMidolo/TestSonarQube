def get_config():
    """
    Crea, completa y devuelve el objeto VersioneerConfig().
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = "0.1.0"
            self.vcs = "git"
            self.tag_prefix = "v"
            self.parentdir_prefix = ""

    config = VersioneerConfig()
    return config