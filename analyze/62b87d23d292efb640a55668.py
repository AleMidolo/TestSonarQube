def get_config():
    """
    Crea, popola e restituisci l'oggetto VersioneerConfig()
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = "1.0.0"
            self.author = "Author Name"
            self.license = "MIT"
            self.description = "A sample project using Versioneer"
    
    config = VersioneerConfig()
    return config