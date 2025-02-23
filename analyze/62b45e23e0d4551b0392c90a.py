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
    
    for version in version_dirs:
        inventory_path = f"{version}/inventory.json"
        try:
            with open(inventory_path, 'r') as f:
                inventory = json.load(f)
                main_inventory[version] = inventory
                
                # Validate that all previous versions have inventories
                if version != version_dirs[0]:
                    previous_version = version_dirs[version_dirs.index(version) - 1]
                    if previous_version not in main_inventory:
                        raise ValueError(f"Missing inventory for previous version: {previous_version}")
                
                # Track content digests
                for item in inventory.get('items', []):
                    content_digest = item.get('digest')
                    if content_digest:
                        if content_digest not in content_digests:
                            content_digests[content_digest] = []
                        content_digests[content_digest].append(version)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Inventory file not found for version: {version}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in inventory file for version: {version}")
    
    return main_inventory, content_digests