def validate_version_inventories(self, version_dirs):
    """
    Ogni versione DOVREBBE avere un inventario fino a quel punto.
    Inoltre, tieni traccia di eventuali digest di contenuto diversi da quelli
    presenti nell'inventario principale, in modo da poterli verificare
    anche durante la validazione del contenuto.

    version_dirs è un array di nomi di directory di versione e si presume
        che sia in sequenza di versione (1, 2, 3...).
    """
    main_inventory = {}
    content_digests = {}
    
    for i, version_dir in enumerate(version_dirs):
        # Simulate loading the inventory for the current version
        current_inventory = self.load_inventory(version_dir)
        
        # Check if the current version has an inventory
        if not current_inventory:
            raise ValueError(f"Missing inventory for version {i + 1} in {version_dir}")
        
        # Validate that all previous versions have inventories
        for j in range(i):
            previous_version_dir = version_dirs[j]
            previous_inventory = self.load_inventory(previous_version_dir)
            if not previous_inventory:
                raise ValueError(f"Missing inventory for version {j + 1} in {previous_version_dir}")
        
        # Track content digests
        for item, digest in current_inventory.items():
            if item in main_inventory:
                if main_inventory[item] != digest:
                    content_digests[item] = digest
            else:
                main_inventory[item] = digest
    
    return main_inventory, content_digests

def load_inventory(self, version_dir):
    # Placeholder for loading inventory logic
    # This should return a dictionary of items and their digests
    return {}