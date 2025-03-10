def get_logical_path_map(inventory, version):
    """
    Obtén un mapa de las rutas lógicas en el estado hacia los archivos en disco para una versión específica en el inventario.

    Devuelve un diccionario: `logical_path_in_state -> set(content_files)`

    El conjunto de `content_files` puede incluir referencias a archivos duplicados en versiones posteriores a la versión que se está describiendo.
    """
    logical_path_map = {}
    
    # Iterar sobre el inventario para encontrar las rutas lógicas y los archivos de contenido
    for logical_path, versions_data in inventory.items():
        if version in versions_data:
            content_files = versions_data[version]
            logical_path_map[logical_path] = set(content_files)
    
    return logical_path_map