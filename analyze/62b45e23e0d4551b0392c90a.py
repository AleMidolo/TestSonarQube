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
        # Assuming each version directory contains an 'inventory.txt' file
        inventory_path = os.path.join(version_dir, 'inventory.txt')
        if not os.path.exists(inventory_path):
            raise FileNotFoundError(f"Inventory file not found in {version_dir}")
        
        with open(inventory_path, 'r') as file:
            current_inventory = set(file.read().splitlines())
        
        # Check if the current inventory is a superset of the previous inventory
        if not current_inventory.issuperset(inventory):
            raise ValueError(f"Inventory in {version_dir} is not a superset of previous inventories")
        
        # Update the main inventory with the current inventory
        inventory.update(current_inventory)
        
        # Track any content digests that are not in the main inventory
        # Assuming content digests are stored in a 'content_digests.txt' file
        content_digests_path = os.path.join(version_dir, 'content_digests.txt')
        if os.path.exists(content_digests_path):
            with open(content_digests_path, 'r') as file:
                content_digests = set(file.read().splitlines())
            
            # Check if any content digest is not in the main inventory
            missing_digests = content_digests - inventory
            if missing_digests:
                raise ValueError(f"Content digests {missing_digests} in {version_dir} are not in the main inventory")
    
    return True