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
    mismatched_digests = []

    for version in version_dirs[1:]:
        current_inventory = self.load_inventory(version)
        if not self.validate_inventory(current_inventory, root_inventory):
            mismatched_digests.append((version, current_inventory.get('digest')))
    
    return mismatched_digests

def load_inventory(self, version_dir):
    # Simulación de carga de inventario
    return {"digest": "some_digest_value"}

def validate_inventory(self, current_inventory, root_inventory):
    # Simulación de validación de inventario
    return current_inventory.get('digest') == root_inventory.get('digest')