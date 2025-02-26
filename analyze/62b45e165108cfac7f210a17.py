def get_logical_path_map(inventory, version):
    """
    Obtén un mapa de las rutas lógicas en el estado hacia los archivos en disco para una versión específica en el inventario.

    Devuelve un diccionario: `logical_path_in_state -> set(content_files)`

    El conjunto de `content_files` puede incluir referencias a archivos duplicados en versiones posteriores a la versión que se está describiendo.
    """
    logical_path_map = {}
    
    for item in inventory:
        if item['version'] == version:
            logical_path = item['logical_path']
            content_file = item['content_file']
            
            if logical_path not in logical_path_map:
                logical_path_map[logical_path] = set()
                
            logical_path_map[logical_path].add(content_file)
    
    return logical_path_map