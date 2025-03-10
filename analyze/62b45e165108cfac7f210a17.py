def get_logical_path_map(inventory, version):
    """
    Get a map of logical paths in state to files on disk for version in inventory.

    Returns a dictionary: logical_path_in_state -> set(content_files)

    The set of content_files may includes references to duplicate files in
    later versions than the version being described.
    """
    logical_path_map = {}
    
    for logical_path, file_versions in inventory.items():
        content_files = set()
        for file_version, file_path in file_versions.items():
            if file_version <= version:
                content_files.add(file_path)
        if content_files:
            logical_path_map[logical_path] = content_files
    
    return logical_path_map