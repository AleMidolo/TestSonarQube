def validate_version_inventories(self, version_dirs):
    """
    Cada versión DEBE tener un inventario hasta ese punto.

    También se debe mantener un registro de cualquier resumen de contenido (digest) 
    que sea diferente de los que están en el inventario raíz, 
    para que también podamos verificarlos al validar el contenido.

    'version_dirs' es un arreglo de nombres de directorios de versiones 
    y se asume que están en secuencia de versiones (1, 2, 3...).
    """
    import os
    from collections import defaultdict

    # Diccionario para almacenar los resúmenes de contenido por versión
    version_digests = defaultdict(dict)

    # Asumimos que el inventario raíz está en el directorio base
    root_inventory = self._load_inventory("root")

    for version_dir in version_dirs:
        # Construir la ruta al inventario de la versión
        inventory_path = os.path.join(version_dir, "inventory.json")
        
        # Verificar si el inventario existe
        if not os.path.exists(inventory_path):
            raise FileNotFoundError(f"El inventario para la versión {version_dir} no existe.")

        # Cargar el inventario de la versión
        version_inventory = self._load_inventory(inventory_path)

        # Comparar los resúmenes de contenido con el inventario raíz
        for item, digest in version_inventory.items():
            if item in root_inventory:
                if digest != root_inventory[item]:
                    version_digests[version_dir][item] = digest
            else:
                version_digests[version_dir][item] = digest

    return version_digests

def _load_inventory(self, path):
    """
    Carga un inventario desde un archivo JSON.
    """
    import json

    with open(path, 'r') as f:
        return json.load(f)