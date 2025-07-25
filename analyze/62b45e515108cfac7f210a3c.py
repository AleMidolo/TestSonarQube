def initialize(self):
    """Crea e inizializza una nuova radice di archiviazione OCFL."""
    import os
    import json

    # Crea la directory radice OCFL
    os.makedirs(self.root_path, exist_ok=True)

    # Crea il file di dichiarazione OCFL
    declaration = {
        "type": "https://ocfl.io/1.0/spec/#inventory",
        "ocfl_version": "1.0",
        "content_directory": "content",
        "digest_algorithm": "sha512",
        "head": None,
        "manifest": {},
        "versions": {}
    }

    with open(os.path.join(self.root_path, "0=ocfl_1.0"), 'w') as f:
        json.dump(declaration, f, indent=4)

    # Crea la directory del contenuto
    os.makedirs(os.path.join(self.root_path, "content"), exist_ok=True)