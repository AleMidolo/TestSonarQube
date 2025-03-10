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
        current_inventory = self.load_inventory(version_dir)
        
        # Check if the current inventory is a superset of the previous inventory
        for key, value in inventory.items():
            if key not in current_inventory or current_inventory[key] != value:
                raise ValueError(f"Inventory mismatch in version {version_dir} for key {key}")
        
        # Update the inventory with the current version's inventory
        inventory.update(current_inventory)
        
        # Track any new content digests that are not in the main inventory
        new_digests = set(current_inventory.keys()) - set(inventory.keys())
        if new_digests:
            print(f"New content digests found in version {version_dir}: {new_digests}")
    
    return inventory