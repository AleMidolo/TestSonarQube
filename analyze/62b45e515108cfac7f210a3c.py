def initialize(self):
    """
    Crear e inicializar una nueva raíz de almacenamiento OCFL.
    """
    # Crear el directorio raíz si no existe
    os.makedirs(self.root_path, exist_ok=True)
    
    # Crear archivo namaste 0=ocfl_1.0
    namaste_path = os.path.join(self.root_path, "0=ocfl_1.0") 
    with open(namaste_path, 'w') as f:
        f.write("ocfl_1.0")
        
    # Crear archivo ocfl_layout.json
    layout = {
        "extension": "0000",
        "description": "Standard OCFL Storage Root",
        "layout": {
            "type": "flat",
            "digest-algorithm": "sha512"
        }
    }
    
    layout_path = os.path.join(self.root_path, "ocfl_layout.json")
    with open(layout_path, 'w') as f:
        json.dump(layout, f, indent=2)
        
    # Crear directorio objects
    objects_path = os.path.join(self.root_path, "objects")
    os.makedirs(objects_path, exist_ok=True)
    
    # Crear directorio extensions
    extensions_path = os.path.join(self.root_path, "extensions") 
    os.makedirs(extensions_path, exist_ok=True)