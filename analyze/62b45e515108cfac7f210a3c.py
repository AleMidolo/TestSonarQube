def initialize(self):
    """Crea e inizializza una nuova radice di archiviazione OCFL."""
    # Create root directory if it doesn't exist
    if not os.path.exists(self.root_path):
        os.makedirs(self.root_path)
    
    # Create namaste file indicating OCFL root
    namaste_path = os.path.join(self.root_path, "0=ocfl_1.0")
    with open(namaste_path, "w") as f:
        f.write("ocfl_1.0")
        
    # Create ocfl_layout.json file
    layout = {
        "extension": "0001-flat-direct-storage-layout",
        "description": "Flat direct storage layout",
        "parameters": {}
    }
    
    layout_path = os.path.join(self.root_path, "ocfl_layout.json") 
    with open(layout_path, "w") as f:
        json.dump(layout, f, indent=2)