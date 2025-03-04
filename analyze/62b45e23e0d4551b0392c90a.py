def validate_version_inventories(self, version_dirs):
    """
    Cada versión DEBE tener un inventario hasta ese punto.

    También se debe mantener un registro de cualquier resumen de contenido (digest) 
    que sea diferente de los que están en el inventorio raíz, 
    para que también podamos verificarlos al validar el contenido.

    'version_dirs' es un arreglo de nombres de directorios de versiones 
    y se asume que están en secuencia de versiones (1, 2, 3...).
    """
    digests_to_verify = set()
    root_inventory = None
    
    # Validar que exista un inventario para cada versión
    for version_dir in version_dirs:
        inventory_path = os.path.join(version_dir, "inventory.txt")
        
        if not os.path.exists(inventory_path):
            raise ValueError(f"No se encontró inventario para la versión {version_dir}")
            
        # Leer el inventario actual
        with open(inventory_path) as f:
            current_inventory = f.read()
            
        # Guardar el inventario raíz (primera versión)
        if root_inventory is None:
            root_inventory = current_inventory
            
        # Comparar digests con el inventario raíz
        current_digests = self._extract_digests(current_inventory)
        root_digests = self._extract_digests(root_inventory)
        
        # Agregar digests diferentes al conjunto a verificar
        for digest in current_digests:
            if digest not in root_digests:
                digests_to_verify.add(digest)
                
    return digests_to_verify

def _extract_digests(self, inventory):
    """Helper method para extraer los digests de un inventario"""
    digests = set()
    for line in inventory.splitlines():
        if line.strip():
            digest = line.split()[0]  # Asume formato "digest filename"
            digests.add(digest)
    return digests