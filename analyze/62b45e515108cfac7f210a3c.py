def initialize(self):
    """
    एक नया OCFL स्टोरेज रूट बनाएँ और प्रारंभ करें।
    """
    # OCFL स्टोरेज रूट बनाने की प्रक्रिया
    self.storage_root = self.create_storage_root()
    self.setup_initial_structure()
    self.initialize_metadata()
    print("OCFL स्टोरेज रूट सफलतापूर्वक बनाया और प्रारंभ किया।")