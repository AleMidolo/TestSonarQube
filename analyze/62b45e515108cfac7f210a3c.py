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
        
    # Create storage root declaration file
    storage_root_path = os.path.join(self.root, "ocfl_1.0.txt") 
    with open(storage_root_path, 'w') as f:
        f.write("This directory is an OCFL Storage Root")
        
    # Create extensions directory
    extensions_dir = os.path.join(self.root, "extensions")
    if not os.path.exists(extensions_dir):
        os.makedirs(extensions_dir)
        
    # Create objects directory
    objects_dir = os.path.join(self.root, "objects") 
    if not os.path.exists(objects_dir):
        os.makedirs(objects_dir)