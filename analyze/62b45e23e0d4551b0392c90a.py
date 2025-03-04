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
        inventory_path = os.path.join(version, "inventory.txt")
        if not os.path.exists(inventory_path):
            raise ValidationError(f"Missing inventory file for version {version}")
            
        # Read inventory and collect content digests
        with open(inventory_path) as f:
            inventory = f.readlines()
            
        for line in inventory:
            if line.strip():
                # Assume inventory line format: filename digest
                filename, digest = line.strip().split()
                content_digests.add(digest)
                
        # Validate version number matches directory name
        try:
            version_num = int(version)
            if version_num != version_dirs.index(version) + 1:
                raise ValidationError(f"Version {version} out of sequence")
        except ValueError:
            raise ValidationError(f"Invalid version directory name: {version}")
            
    # Store unique content digests for later validation
    self.content_digests = content_digests
    
    return True