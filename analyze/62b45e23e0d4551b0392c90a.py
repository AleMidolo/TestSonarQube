def validate_version_inventories(self, version_dirs):
    """
    Ogni versione DOVREBBE avere un inventario fino a quel punto.
    Inoltre, tieni traccia di eventuali digest di contenuto diversi da quelli
    presenti nell'inventario principale, in modo da poterli verificare
    anche durante la validazione del contenuto.

      version_dirs è un array di nomi di directory di versione e si presume
        che sia in sequenza di versione (1, 2, 3...).
    """
    inventory_digests = {}
    for i, version_dir in enumerate(version_dirs):
        # Simulate loading the inventory for the current version
        inventory = self.load_inventory(version_dir)
        
        # Check if the inventory is valid
        if not self.is_valid_inventory(inventory):
            raise ValueError(f"Invalid inventory for version {version_dir}")
        
        # Track the digest of the current inventory
        current_digest = self.calculate_digest(inventory)
        inventory_digests[version_dir] = current_digest
        
        # Ensure all previous versions have inventories
        for j in range(i):
            previous_version_dir = version_dirs[j]
            if previous_version_dir not in inventory_digests:
                raise ValueError(f"Missing inventory for version {previous_version_dir}")
    
    return inventory_digests

def load_inventory(self, version_dir):
    # Placeholder for loading inventory logic
    pass

def is_valid_inventory(self, inventory):
    # Placeholder for inventory validation logic
    pass

def calculate_digest(self, inventory):
    # Placeholder for digest calculation logic
    pass