def get_logical_path_map(inventory, version):
    """
    Get a map of logical paths in state to files on disk for version in inventory.

    Returns a dictionary: logical_path_in_state -> set(content_files)

    The set of content_files may includes references to duplicate files in
    later versions than the version being described.
    """
    logical_path_map = {}
    
    # Iterate through all versions up to and including target version
    for ver in range(version + 1):
        if ver in inventory:
            # For each file in this version
            for logical_path, content_files in inventory[ver].items():
                # Add or update the set of content files for this logical path
                if logical_path not in logical_path_map:
                    logical_path_map[logical_path] = set()
                logical_path_map[logical_path].update(content_files)
                
    return logical_path_map