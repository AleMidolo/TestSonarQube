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
        if not all(item in current_inventory for item in inventory):
            raise ValueError(f"Inventory for version {version_dir} is not a superset of the previous inventory.")
        
        # Update the inventory with the current version's inventory
        inventory.update(current_inventory)
        
        # Track any content digests that differ from the main inventory
        differing_digests = {k: v for k, v in current_inventory.items() if k in inventory and inventory[k] != v}
        if differing_digests:
            self.log_differing_digests(version_dir, differing_digests)
    
    return inventory