def initialize(self):
    """
    Create and initialize a new OCFL storage root.
    """
    # Create root directory if it doesn't exist
    os.makedirs(self.storage_root, exist_ok=True)
    
    # Create OCFL storage root marker file (0=ocfl_1.0)
    namaste_file = os.path.join(self.storage_root, "0=ocfl_1.0")
    with open(namaste_file, 'w') as f:
        f.write("ocfl_1.0")
        
    # Create ocfl_layout.json file
    layout_file = os.path.join(self.storage_root, "ocfl_layout.json")
    layout_content = {
        "extension": "000",
        "description": "OCFL Storage Root",
        "layout": {
            "type": "flat",
            "pattern": "^[a-f0-9]{2}/[a-f0-9]{2}/[a-f0-9]{2}/[a-f0-9]{58}$"
        }
    }
    
    with open(layout_file, 'w') as f:
        json.dump(layout_content, f, indent=2)
        
    # Create extensions directory
    extensions_dir = os.path.join(self.storage_root, "extensions")
    os.makedirs(extensions_dir, exist_ok=True)