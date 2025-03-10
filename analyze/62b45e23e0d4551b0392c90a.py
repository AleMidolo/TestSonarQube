def validate_version_inventories(self, version_dirs):
    """
    Ogni versione DOVREBBE avere un inventario fino a quel punto.
    Inoltre, tieni traccia di eventuali digest di contenuto diversi da quelli
    presenti nell'inventario principale, in modo da poterli verificare
    anche durante la validazione del contenuto.

    version_dirs è un array di nomi di directory di versione e si presume
    che sia in sequenza di versione (1, 2, 3...).
    """
    inventory = set()
    for version_dir in version_dirs:
        # Load the inventory for the current version
        current_inventory = self._load_inventory(version_dir)
        
        # Check if the current inventory is a superset of the previous inventory
        if not inventory.issubset(current_inventory):
            raise ValueError(f"Inventory for version {version_dir} is not a superset of previous versions.")
        
        # Update the inventory with the current version's inventory
        inventory.update(current_inventory)
        
        # Track any content digests that differ from the main inventory
        self._track_different_digests(current_inventory, inventory)
    
    return True

def _load_inventory(self, version_dir):
    """
    Load the inventory for a specific version directory.
    """
    # Placeholder for loading inventory from the version directory
    # This should return a set of content digests
    return set()

def _track_different_digests(self, current_inventory, main_inventory):
    """
    Track any content digests that differ from the main inventory.
    """
    # Placeholder for tracking different digests
    pass