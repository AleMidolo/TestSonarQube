def validate_version_inventories(self, version_dirs):
    """
    Ogni versione DOVREBBE avere un inventario fino a quel punto.
    Inoltre, tieni traccia di eventuali digest di contenuto diversi da quelli
    presenti nell'inventario principale, in modo da poterli verificare
    anche durante la validazione del contenuto.

    version_dirs è un array di nomi di directory di versione e si presume
    che sia in sequenza di versione (1, 2, 3...).
    """
    for i, version_dir in enumerate(version_dirs):
        # Check if the version directory exists
        if not os.path.exists(version_dir):
            raise FileNotFoundError(f"Version directory {version_dir} does not exist.")
        
        # Check if the inventory file exists in the version directory
        inventory_file = os.path.join(version_dir, "inventory.txt")
        if not os.path.exists(inventory_file):
            raise FileNotFoundError(f"Inventory file not found in {version_dir}.")
        
        # Read the inventory file
        with open(inventory_file, 'r') as file:
            inventory_content = file.read().splitlines()
        
        # Validate the inventory content
        for line in inventory_content:
            if not line.strip():
                continue  # Skip empty lines
            # Example validation: check if the line contains a valid digest
            if not line.startswith("digest:"):
                raise ValueError(f"Invalid inventory line in {version_dir}: {line}")
        
        # Track any content digests that differ from the main inventory
        if i > 0:
            previous_inventory_file = os.path.join(version_dirs[i-1], "inventory.txt")
            with open(previous_inventory_file, 'r') as file:
                previous_inventory_content = file.read().splitlines()
            
            # Compare current inventory with previous inventory
            if set(inventory_content) != set(previous_inventory_content):
                # Log or handle differences
                print(f"Differences found between {version_dirs[i-1]} and {version_dir}")