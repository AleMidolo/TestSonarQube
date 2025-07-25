def get_config():
    """
    Crea, completa y devuelve el objeto VersioneerConfig().
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = "1.0.0"
            self.description = "Default configuration for Versioneer"
            self.author = "Unknown"
            self.license = "MIT"
    
    config = VersioneerConfig()
    return config