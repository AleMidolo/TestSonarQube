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
    
    # Validar que exista un inventario para cada versión
    for version_dir in version_dirs:
        inventory_path = os.path.join(version_dir, "inventory.txt")
        
        if not os.path.exists(inventory_path):
            raise ValueError(f"No se encontró inventario para la versión {version_dir}")
            
        # Leer el inventario de la versión actual
        with open(inventory_path) as f:
            version_inventory = f.readlines()
            
        # Obtener los digests del inventario actual
        version_digests = set()
        for line in version_inventory:
            if line.strip():
                digest = line.split()[0]
                version_digests.add(digest)
                
        # Comparar con el inventario raíz y agregar digests diferentes
        root_inventory_path = "inventory.txt"
        if os.path.exists(root_inventory_path):
            with open(root_inventory_path) as f:
                root_inventory = f.readlines()
                
            root_digests = set()
            for line in root_inventory:
                if line.strip():
                    digest = line.split()[0] 
                    root_digests.add(digest)
                    
            # Agregar digests que son diferentes al inventario raíz
            different_digests = version_digests - root_digests
            digests_to_verify.update(different_digests)
                
    return digests_to_verify