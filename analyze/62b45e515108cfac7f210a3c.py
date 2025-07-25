def initialize(self):
    """Crea e inizializza una nuova radice di archiviazione OCFL."""
    import os
    import json

    # Crea la directory radice OCFL
    os.makedirs(self.root_path, exist_ok=True)

    # Crea il file di configurazione OCFL
    config = {
        "ocfl-version": "1.0",
        "type": "https://ocfl.io/1.0/spec/#inventory",
        "digestAlgorithm": "sha512",
        "contentDirectory": "content",
        "manifest": {},
        "versions": {}
    }

    with open(os.path.join(self.root_path, "0=ocfl_1.0"), 'w') as f:
        json.dump(config, f, indent=4)

    # Crea la directory per il contenuto
    os.makedirs(os.path.join(self.root_path, "content"), exist_ok=True)

    # Crea il file di inventario iniziale
    inventory = {
        "id": "urn:uuid:12345678-1234-5678-1234-567812345678",
        "type": "https://ocfl.io/1.0/spec/#inventory",
        "digestAlgorithm": "sha512",
        "head": "v1",
        "versions": {
            "v1": {
                "created": "2023-10-01T00:00:00Z",
                "state": {},
                "message": "Initial version"
            }
        },
        "manifest": {}
    }

    with open(os.path.join(self.root_path, "inventory.json"), 'w') as f:
        json.dump(inventory, f, indent=4)