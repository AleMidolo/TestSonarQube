def validate_version_inventories(self, version_dirs):
    """
    Ogni versione DOVREBBE avere un inventario fino a quel punto.
    Inoltre, tieni traccia di eventuali digest di contenuto diversi da quelli
    presenti nell'inventario principale, in modo da poterli verificare
    anche durante la validazione del contenuto.

    version_dirs è un array di nomi di directory di versione e si presume
    che sia in sequenza di versione (1, 2, 3...).
    """
    inventories = {}
    for version_dir in version_dirs:
        inventory_path = os.path.join(version_dir, "inventory.json")
        if not os.path.exists(inventory_path):
            raise FileNotFoundError(f"Inventory not found for version: {version_dir}")
        
        with open(inventory_path, 'r') as f:
            inventory = json.load(f)
        
        inventories[version_dir] = inventory
        
        # Check for discrepancies in content digests
        if version_dir != version_dirs[0]:  # Skip the first version
            previous_version = version_dirs[version_dirs.index(version_dir) - 1]
            previous_inventory = inventories[previous_version]
            
            for key, value in inventory.items():
                if key in previous_inventory and previous_inventory[key] != value:
                    print(f"Warning: Content digest mismatch for {key} in {version_dir}")
    
    return inventories