def get_config():
    """
    Crea, popola e restituisci l'oggetto VersioneerConfig()
    """
    class VersioneerConfig:
        def __init__(self):
            self.version = "1.0.0"
            self.author = "Author Name"
            self.license = "MIT"
            self.description = "This is a sample configuration object."

    config = VersioneerConfig()
    # Populating the config object with additional data if needed
    # config.some_property = "Some Value"
    
    return config