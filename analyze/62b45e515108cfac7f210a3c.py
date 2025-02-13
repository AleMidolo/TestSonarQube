def initialize(self):
    """Crea e inizializza una nuova radice di archiviazione OCFL."""
    self.root = {}
    self.version = 1.0
    self.metadata = {
        "created": datetime.now(),
        "format": "OCFL",
        "version": self.version
    }
    return self.root