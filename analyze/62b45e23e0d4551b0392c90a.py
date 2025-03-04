def validate_version_inventories(self, version_dirs):
    """
    Ogni versione DOVREBBE avere un inventario fino a quel punto.
    Inoltre, tieni traccia di eventuali digest di contenuto diversi da quelli
    presenti nell'inventario principale, in modo da poterli verificare
    anche durante la validazione del contenuto.

    version_dirs è un array di nomi di directory di versione e si presume
      che sia in sequenza di versione (1, 2, 3...).
    """
    content_digests = set()
    
    # Validate each version has an inventory
    for version in version_dirs:
        inventory_path = os.path.join(version, 'inventory.txt')
        if not os.path.exists(inventory_path):
            raise ValidationError(f"Missing inventory file for version {version}")
            
        # Read inventory and collect content digests
        with open(inventory_path) as f:
            inventory = f.readlines()
            
        for line in inventory:
            if line.strip():
                try:
                    filename, digest = line.strip().split()
                    content_digests.add(digest)
                except ValueError:
                    raise ValidationError(f"Invalid inventory line in {version}: {line}")
                    
    # Compare with main inventory
    main_inventory_path = 'inventory.txt'
    if os.path.exists(main_inventory_path):
        with open(main_inventory_path) as f:
            main_inventory = f.readlines()
            
        main_digests = set()
        for line in main_inventory:
            if line.strip():
                try:
                    filename, digest = line.strip().split()
                    main_digests.add(digest)
                except ValueError:
                    raise ValidationError(f"Invalid line in main inventory: {line}")
                    
        # Check for digests not in main inventory
        diff_digests = content_digests - main_digests
        if diff_digests:
            self.extra_digests = diff_digests
            
    return True