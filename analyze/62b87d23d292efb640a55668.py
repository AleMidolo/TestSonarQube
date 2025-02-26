def get_config():
    """
    Create, populate and return the VersioneerConfig() object.
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = "1.0.0"
            self.author = "Your Name"
            self.email = "your.email@example.com"
            self.license = "MIT"
            self.description = "A sample project using Versioneer"
    
    config = VersioneerConfig()
    return config