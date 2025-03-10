def validate_version_inventories(self, version_dirs):
    """
    Cada versión DEBE tener un inventario hasta ese punto.

    También se debe mantener un registro de cualquier resumen de contenido (digest) 
    que sea diferente de los que están en el inventario raíz, 
    para que también podamos verificarlos al validar el contenido.

    'version_dirs' es un arreglo de nombres de directorios de versiones 
    y se asume que están en secuencia de versiones (1, 2, 3...).
    """
    for version_dir in version_dirs:
        inventory_path = os.path.join(version_dir, "inventory.json")
        if not os.path.exists(inventory_path):
            raise FileNotFoundError(f"Inventory not found for version: {version_dir}")
        
        with open(inventory_path, 'r') as f:
            inventory = json.load(f)
        
        # Check for any digests that differ from the root inventory
        root_inventory_path = os.path.join(version_dirs[0], "inventory.json")
        with open(root_inventory_path, 'r') as f:
            root_inventory = json.load(f)
        
        for key, value in inventory.items():
            if key in root_inventory and value != root_inventory[key]:
                print(f"Warning: Digest mismatch for {key} in version {version_dir}")