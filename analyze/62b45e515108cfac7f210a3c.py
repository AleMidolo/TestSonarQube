def initialize(self):
    """
    Crear e inicializar una nueva raíz de almacenamiento OCFL.
    """
    # Crear el directorio raíz si no existe
    if not os.path.exists(self.root_path):
        os.makedirs(self.root_path)

    # Crear archivo namaste 0=ocfl_1.0
    namaste_path = os.path.join(self.root_path, "0=ocfl_1.0")
    with open(namaste_path, 'w') as f:
        f.write("ocfl_1.0")

    # Crear archivo ocfl_layout.json
    layout = {
        "extension": "0000",
        "description": "OCFL Storage Root",
        "type": "https://ocfl.io/1.0/spec/#root",
        "created": datetime.datetime.now().isoformat()
    }

    layout_path = os.path.join(self.root_path, "ocfl_layout.json")
    with open(layout_path, 'w') as f:
        json.dump(layout, f, indent=2)

    # Crear directorio de objetos
    objects_dir = os.path.join(self.root_path, "objects")
    if not os.path.exists(objects_dir):
        os.makedirs(objects_dir)

    # Crear directorio de extensiones
    extensions_dir = os.path.join(self.root_path, "extensions") 
    if not os.path.exists(extensions_dir):
        os.makedirs(extensions_dir)