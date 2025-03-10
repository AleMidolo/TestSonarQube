def validate_version_inventories(self, version_dirs):
    """
    Cada versión DEBE tener un inventario hasta ese punto.

    También se debe mantener un registro de cualquier resumen de contenido (digest) 
    que sea diferente de los que están en el inventario raíz, 
    para que también podamos verificarlos al validar el contenido.

    'version_dirs' es un arreglo de nombres de directorios de versiones 
    y se asume que están en secuencia de versiones (1, 2, 3...).
    """
    root_inventory = self._load_root_inventory()  # Load the root inventory
    previous_inventory = root_inventory
    discrepancies = {}

    for version_dir in version_dirs:
        version_inventory = self._load_version_inventory(version_dir)
        
        # Check if the version has an inventory
        if not version_inventory:
            raise ValueError(f"Version {version_dir} does not have an inventory.")
        
        # Compare with the previous inventory
        diff = self._compare_inventories(previous_inventory, version_inventory)
        if diff:
            discrepancies[version_dir] = diff
        
        # Update the previous inventory for the next iteration
        previous_inventory = version_inventory

    return discrepancies

def _load_root_inventory(self):
    """
    Load the root inventory.
    """
    # Implementation to load the root inventory
    pass

def _load_version_inventory(self, version_dir):
    """
    Load the inventory for a specific version directory.
    """
    # Implementation to load the version inventory
    pass

def _compare_inventories(self, inv1, inv2):
    """
    Compare two inventories and return the differences.
    """
    # Implementation to compare inventories
    pass