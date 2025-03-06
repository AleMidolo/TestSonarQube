def validate_version_inventories(self, version_dirs):
    """
    Cada versión DEBE tener un inventario hasta ese punto.

    También se debe mantener un registro de cualquier resumen de contenido (digest) 
    que sea diferente de los que están en el inventario raíz, 
    para que también podamos verificarlos al validar el contenido.

    'version_dirs' es un arreglo de nombres de directorios de versiones 
    y se asume que están en secuencia de versiones (1, 2, 3...).
    """
    if not version_dirs:
        raise ValueError("No version directories provided.")
    
    # Assuming the root inventory is in the first version directory
    root_inventory = self._load_inventory(version_dirs[0])
    if not root_inventory:
        raise ValueError("Root inventory is missing or empty.")
    
    # Track digests that differ from the root inventory
    differing_digests = {}
    
    for version_dir in version_dirs:
        current_inventory = self._load_inventory(version_dir)
        if not current_inventory:
            raise ValueError(f"Inventory missing in version directory: {version_dir}")
        
        # Compare digests with the root inventory
        for item, digest in current_inventory.items():
            if item in root_inventory:
                if digest != root_inventory[item]:
                    differing_digests[item] = digest
            else:
                differing_digests[item] = digest
    
    return differing_digests

def _load_inventory(self, version_dir):
    """
    Helper method to load the inventory from a version directory.
    This is a placeholder and should be implemented based on the actual inventory format.
    """
    # Placeholder implementation
    # In a real scenario, this would load the inventory from the directory
    return {}