def validate_version_inventories(self, version_dirs):
    """
    Cada versión DEBE tener un inventario hasta ese punto.

    También se debe mantener un registro de cualquier resumen de contenido (digest) 
    que sea diferente de los que están en el inventario raíz, 
    para que también podamos verificarlos al validar el contenido.

    'version_dirs' es un arreglo de nombres de directorios de versiones 
    y se asume que están en secuencia de versiones (1, 2, 3...).
    """
    root_inventory = self.load_inventory(version_dirs[0])
    mismatched_digests = {}

    for version in version_dirs:
        current_inventory = self.load_inventory(version)
        
        if not self.validate_inventory(current_inventory):
            raise ValueError(f"Invalid inventory for version: {version}")
        
        for item, digest in current_inventory.items():
            if item in root_inventory and root_inventory[item] != digest:
                mismatched_digests[item] = {
                    'root_digest': root_inventory[item],
                    'current_digest': digest,
                    'version': version
                }

    return mismatched_digests

def load_inventory(self, version):
    # Simulated method to load inventory for a given version
    pass

def validate_inventory(self, inventory):
    # Simulated method to validate the inventory structure
    return True