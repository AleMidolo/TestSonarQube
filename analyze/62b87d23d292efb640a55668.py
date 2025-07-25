def get_config():
    """
    Crea, completa y devuelve el objeto VersioneerConfig().
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = "1.0.0"
            self.author = "Unknown"
            self.description = "Default configuration for Versioneer"

        def __repr__(self):
            return f"VersioneerConfig(version={self.version}, author={self.author}, description={self.description})"

    config = VersioneerConfig()
    return config