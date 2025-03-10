def validate_version_inventories(self, version_dirs):
    """
    Ogni versione DOVREBBE avere un inventario fino a quel punto.
    Inoltre, tieni traccia di eventuali digest di contenuto diversi da quelli
    presenti nell'inventario principale, in modo da poterli verificare
    anche durante la validazione del contenuto.

    version_dirs è un array di nomi di directory di versione e si presume
    che sia in sequenza di versione (1, 2, 3...).
    """
    inventory = {}
    for version_dir in version_dirs:
        # Load the inventory for the current version
        current_inventory = self._load_inventory(version_dir)
        
        # Check if the current inventory is consistent with the previous one
        for key, value in current_inventory.items():
            if key in inventory and inventory[key] != value:
                raise ValueError(f"Content digest mismatch for {key} in version {version_dir}")
        
        # Update the main inventory with the current version's inventory
        inventory.update(current_inventory)
    
    return inventory

def _load_inventory(self, version_dir):
    """
    Helper function to load the inventory from a version directory.
    This is a placeholder and should be implemented based on the actual inventory format.
    """
    # Placeholder implementation
    return {}