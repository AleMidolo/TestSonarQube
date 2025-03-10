def initialize(self):
    """Crea e inizializza una nuova radice di archiviazione OCFL."""
    import os
    import json

    # Crea la directory radice OCFL
    os.makedirs(self.root_path, exist_ok=True)

    # Crea il file di dichiarazione OCFL
    declaration = {
        "type": "https://ocfl.io/1.0/spec/#inventory",
        "digestAlgorithm": "sha512",
        "head": None,
        "versions": {}
    }

    with open(os.path.join(self.root_path, "0=ocfl_object_1.0"), 'w') as f:
        f.write("ocfl_object_1.0\n")

    with open(os.path.join(self.root_path, "inventory.json"), 'w') as f:
        json.dump(declaration, f, indent=4)

    # Crea la directory per le versioni
    os.makedirs(os.path.join(self.root_path, "v1"), exist_ok=True)