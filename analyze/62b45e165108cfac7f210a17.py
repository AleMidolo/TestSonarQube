def get_logical_path_map(inventory, version):
    """
    Get a map of logical paths in state to files on disk for version in inventory.

    Returns a dictionary: logical_path_in_state -> set(content_files)

    The set of content_files may includes references to duplicate files in
    later versions than the version being described.
    """
    logical_path_map = {}
    
    for logical_path, versions in inventory.items():
        content_files = set()
        for v, files in versions.items():
            if v >= version:
                content_files.update(files)
        if content_files:
            logical_path_map[logical_path] = content_files
    
    return logical_path_map