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
        
        # Check if the current inventory is valid
        if not self.is_valid_inventory(current_inventory):
            raise ValueError(f"Invalid inventory for version {version_dir}")
        
        # Update the main inventory with the current version's inventory
        main_inventory.update(current_inventory)
        
        # Track content digests
        for item, digest in current_inventory.items():
            if item in content_digests:
                if content_digests[item] != digest:
                    print(f"Content digest mismatch for {item} in version {version_dir}")
            else:
                content_digests[item] = digest
        
        # Ensure all previous versions have been accounted for
        if i > 0:
            previous_inventory = self.load_inventory(version_dirs[i - 1])
            if not self.is_inventory_subset(previous_inventory, current_inventory):
                raise ValueError(f"Version {version_dirs[i - 1]} is not a subset of {version_dir}")
    
    return main_inventory

def load_inventory(self, version_dir):
    # Placeholder for loading inventory logic
    pass

def is_valid_inventory(self, inventory):
    # Placeholder for inventory validation logic
    return True

def is_inventory_subset(self, previous_inventory, current_inventory):
    # Placeholder for subset checking logic
    return all(item in current_inventory for item in previous_inventory)