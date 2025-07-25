def get_logical_path_map(inventory, version):
    """
    Ottiene una mappa dei percorsi logici nello stato verso i file su disco per una determinata versione nell'inventario.

    Restituisce un dizionario: `logical_path_in_state -> set(content_files)`

    Il set di `content_files` può includere riferimenti a file duplicati presenti in versioni successive rispetto alla versione descritta.
    """
    logical_path_map = {}
    
    for logical_path, versions in inventory.items():
        if version in versions:
            content_files = set()
            for v in range(version, max(versions.keys()) + 1):
                if v in versions:
                    content_files.update(versions[v])
            logical_path_map[logical_path] = content_files
    
    return logical_path_map