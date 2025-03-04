def initialize(self):
    """
    Crear e inicializar una nueva raíz de almacenamiento OCFL.
    """
    # Crear el directorio raíz si no existe
    if not os.path.exists(self.root_path):
        os.makedirs(self.root_path)

    # Crear archivo namaste que identifica el directorio como raíz OCFL
    namaste_path = os.path.join(self.root_path, "0=ocfl_1.0")
    with open(namaste_path, "w") as f:
        f.write("ocfl_1.0")

    # Crear directorio de objetos
    objects_dir = os.path.join(self.root_path, "objects")
    if not os.path.exists(objects_dir):
        os.makedirs(objects_dir)

    # Crear archivo de configuración ocfl_layout.json
    layout_config = {
        "extension": "0001-pairtree-storage-layout",
        "description": "Pairtree directory layout"
    }
    layout_path = os.path.join(self.root_path, "ocfl_layout.json") 
    with open(layout_path, "w") as f:
        json.dump(layout_config, f, indent=2)