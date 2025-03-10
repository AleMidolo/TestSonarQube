def get_config():
    """
    Crea, completa y devuelve el objeto VersioneerConfig().
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = "0.1.0"
            self.description = "Versioneer configuration object"
            self.author = "Unknown"
            self.license = "MIT"
    
    config = VersioneerConfig()
    return config