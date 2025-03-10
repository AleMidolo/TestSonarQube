def initialize(self):
    """
    Crea e inizializza una nuova radice di archiviazione OCFL.
    """
    import os

    # Crea la directory radice OCFL
    os.makedirs("ocfl_root", exist_ok=True)

    # Crea il file di dichiarazione OCFL
    with open(os.path.join("ocfl_root", "0=ocfl_object_1.0"), "w") as f:
        f.write("ocfl_1.0\n")

    # Crea la directory per gli oggetti OCFL
    os.makedirs(os.path.join("ocfl_root", "objects"), exist_ok=True)

    # Crea il file di inventario
    with open(os.path.join("ocfl_root", "inventory.json"), "w") as f:
        f.write('{"head": "v1", "versions": {}}')

    print("Radice OCFL inizializzata con successo.")