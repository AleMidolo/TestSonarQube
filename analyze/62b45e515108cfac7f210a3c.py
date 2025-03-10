def initialize(self):
    """
    Crea e inizializza una nuova radice di archiviazione OCFL.
    """
    import os

    # Crea la directory radice OCFL
    if not os.path.exists(self.root_path):
        os.makedirs(self.root_path)

    # Crea il file di dichiarazione OCFL
    declaration_path = os.path.join(self.root_path, "0=ocfl_1.0")
    with open(declaration_path, "w") as f:
        f.write("ocfl_1.0\n")

    # Crea la directory per gli oggetti OCFL
    objects_path = os.path.join(self.root_path, "objects")
    if not os.path.exists(objects_path):
        os.makedirs(objects_path)

    # Crea la directory per i file di log
    logs_path = os.path.join(self.root_path, "logs")
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)