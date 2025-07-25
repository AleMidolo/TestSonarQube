def initialize(self):
    """
    Crear e inicializar una nueva raíz de almacenamiento OCFL.
    """
    import os
    import json

    # Crear la estructura de directorios básica
    os.makedirs("ocfl_root", exist_ok=True)
    os.makedirs("ocfl_root/objects", exist_ok=True)
    os.makedirs("ocfl_root/extensions", exist_ok=True)

    # Crear el archivo de configuración OCFL
    config = {
        "type": "https://ocfl.io/1.0/spec/#inventory",
        "digestAlgorithm": "sha512",
        "head": None,
        "versions": []
    }

    with open("ocfl_root/ocfl_config.json", "w") as config_file:
        json.dump(config, config_file, indent=4)

    print("Raíz de almacenamiento OCFL inicializada correctamente.")