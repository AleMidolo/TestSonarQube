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
        
        # Check if the current version inventory is valid
        if i > 0:
            previous_inventory = self.load_inventory(version_dirs[i - 1])
            if not self.is_valid_inventory(previous_inventory, current_inventory):
                raise ValueError(f"Invalid inventory for version {version_dir}")
        
        # Track content digests
        for item in current_inventory:
            digest = self.calculate_digest(item)
            if item in main_inventory:
                if main_inventory[item] != digest:
                    content_digests[item] = digest
            else:
                main_inventory[item] = digest

    return main_inventory, content_digests

def load_inventory(self, version_dir):
    # Placeholder for loading inventory logic
    pass

def is_valid_inventory(self, previous_inventory, current_inventory):
    # Placeholder for inventory validation logic
    pass

def calculate_digest(self, item):
    # Placeholder for digest calculation logic
    pass