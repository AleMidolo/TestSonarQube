def get_logical_path_map(inventory, version):
    """
    Get a map of logical paths in state to files on disk for version in inventory.

    Returns a dictionary: logical_path_in_state -> set(content_files)

    The set of content_files may includes references to duplicate files in
    later versions than the version being described.
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