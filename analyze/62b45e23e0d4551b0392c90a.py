def validate_version_inventories(self, version_dirs):
    """
    Cada versión DEBE tener un inventario hasta ese punto.

    También se debe mantener un registro de cualquier resumen de contenido (digest) 
    que sea diferente de los que están en el inventario raíz, 
    para que también podamos verificarlos al validar el contenido.

    'version_dirs' es un arreglo de nombres de directorios de versiones 
    y se asume que están en secuencia de versiones (1, 2, 3...).
    """
    root_inventory = self.get_root_inventory()  # Assume this method exists to get the root inventory
    discrepancies = {}

    for version_dir in version_dirs:
        version_inventory = self.get_version_inventory(version_dir)  # Assume this method exists to get the version inventory
        
        # Check if the version inventory exists
        if not version_inventory:
            raise ValueError(f"Version {version_dir} does not have an inventory.")
        
        # Compare with root inventory and record discrepancies
        for key, value in version_inventory.items():
            if key in root_inventory and root_inventory[key] != value:
                if version_dir not in discrepancies:
                    discrepancies[version_dir] = {}
                discrepancies[version_dir][key] = value
    
    return discrepancies