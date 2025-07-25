def initialize(self):
    """
    एक नया OCFL स्टोरेज रूट बनाएँ और प्रारंभ करें।
    """
    # Create root directory if it doesn't exist
    if not os.path.exists(self.root):
        os.makedirs(self.root)

    # Create namaste file
    namaste_path = os.path.join(self.root, "0=ocfl_1.0")
    with open(namaste_path, 'w') as f:
        f.write("ocfl_1.0")

    # Create ocfl_layout.json file
    layout = {
        "extension": "0001-flat-direct-storage-layout",
        "description": "Flat direct storage layout",
        "layout": {
            "type": "flat",
            "delimiter": "/"
        }
    }
    
    layout_path = os.path.join(self.root, "ocfl_layout.json")
    with open(layout_path, 'w') as f:
        json.dump(layout, f, indent=2)