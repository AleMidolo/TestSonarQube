def get_logical_path_map(inventory, version):
    """
    Ottiene una mappa dei percorsi logici nello stato verso i file su disco per una determinata versione nell'inventario.

    Restituisce un dizionario: `logical_path_in_state -> set(content_files)`

    Il set di `content_files` può includere riferimenti a file duplicati presenti in versioni successive rispetto alla versione descritta.
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