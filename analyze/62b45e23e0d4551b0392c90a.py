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
        inventory_path = f"{version_dir}/inventory.json"
        try:
            with open(inventory_path, 'r') as f:
                inventory = json.load(f)
                main_inventory.update(inventory)
                
                # Verifica che tutte le versioni precedenti abbiano un inventario
                if i > 0:
                    previous_inventory_path = f"{version_dirs[i-1]}/inventory.json"
                    if not os.path.exists(previous_inventory_path):
                        raise ValueError(f"Missing inventory for version {version_dirs[i-1]}")
                
                # Controlla i digest di contenuto
                for item in inventory.get('items', []):
                    content_digest = item.get('digest')
                    if content_digest and content_digest not in content_digests:
                        content_digests[content_digest] = version_dir
                    elif content_digest:
                        if content_digests[content_digest] != version_dir:
                            print(f"Content digest {content_digest} differs between versions {content_digests[content_digest]} and {version_dir}")

        except FileNotFoundError:
            raise FileNotFoundError(f"Inventory file not found for version {version_dir}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in inventory file for version {version_dir}")