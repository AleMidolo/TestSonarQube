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
        "contentDirectory": "content",
        "id": "urn:uuid:12345678-1234-5678-1234-567812345678",
        "head": "v1",
        "versions": {
            "v1": {
                "created": "2023-10-01T00:00:00Z",
                "state": {},
                "message": "Initial version"
            }
        }
    }

    with open(os.path.join(self.root_path, "0=ocfl_object_1.0"), 'w') as f:
        f.write("ocfl_object_1.0\n")

    with open(os.path.join(self.root_path, "inventory.json"), 'w') as f:
        json.dump(declaration, f, indent=4)

    # Crea la directory del contenuto
    os.makedirs(os.path.join(self.root_path, "content"), exist_ok=True)