def initialize(self):
    """
    Create and initialize a new OCFL storage root.
    """
    # Create root directory if it doesn't exist
    os.makedirs(self.storage_root, exist_ok=True)
    
    # Create namaste file identifying this as OCFL storage root
    namaste_path = os.path.join(self.storage_root, "0=ocfl_1.0")
    with open(namaste_path, 'w') as f:
        f.write("ocfl_1.0")
        
    # Create ocfl_layout.json file
    layout = {
        "extension": "000",
        "description": "OCFL Storage Root",
        "layout": {
            "type": "flat",
            "pattern": "{object-id}"
        }
    }
    
    layout_path = os.path.join(self.storage_root, "ocfl_layout.json")
    with open(layout_path, 'w') as f:
        json.dump(layout, f, indent=2)
        
    # Create extensions directory
    extensions_dir = os.path.join(self.storage_root, "extensions")
    os.makedirs(extensions_dir, exist_ok=True)