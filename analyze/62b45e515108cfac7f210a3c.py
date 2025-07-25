def initialize(self):
    """
    Create and initialize a new OCFL storage root.
    """
    # Create root directory if it doesn't exist
    os.makedirs(self.storage_root, exist_ok=True)
    
    # Create OCFL storage root marker file (namaste)
    with open(os.path.join(self.storage_root, "0=ocfl_1.0"), "w") as f:
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
    
    with open(os.path.join(self.storage_root, "ocfl_layout.json"), "w") as f:
        json.dump(layout, f, indent=2)