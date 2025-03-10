def get_config():
    """
    Crea, popola e restituisci l'oggetto VersioneerConfig()
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = "1.0.0"
            self.description = "Default configuration for Versioneer"
            self.author = "Unknown"
            self.license = "MIT"
        
        def __repr__(self):
            return f"VersioneerConfig(version={self.version}, description={self.description}, author={self.author}, license={self.license})"
    
    config = VersioneerConfig()
    return config