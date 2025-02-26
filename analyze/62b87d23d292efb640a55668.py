def get_config():
    """
    Crea, completa y devuelve el objeto VersioneerConfig().
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = None
            self.tag_prefix = None
            self.vcs = None

    config = VersioneerConfig()
    config.version = "0.1.0"
    config.tag_prefix = "v"
    config.vcs = "git"
    
    return config