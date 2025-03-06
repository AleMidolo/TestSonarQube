def get_logical_path_map(inventory, version):
    """
    Get a map of logical paths in state to files on disk for version in inventory.

    Returns a dictionary: logical_path_in_state -> set(content_files)

    The set of content_files may includes references to duplicate files in
    later versions than the version being described.
    """
    logical_path_map = {}
    
    for item in inventory:
        if item['version'] == version:
            logical_path = item['logical_path']
            content_files = set(item['content_files'])
            
            if logical_path in logical_path_map:
                logical_path_map[logical_path].update(content_files)
            else:
                logical_path_map[logical_path] = content_files
    
    return logical_path_map