def get_logical_path_map(inventory, version):
    logical_path_map = {}
    
    # Get all content files for this version and later versions
    content_files = set()
    for v in inventory.versions:
        if v >= version:
            content_files.update(inventory.get_content_files(v))
            
    # Build mapping of logical paths to content files
    for logical_path in inventory.get_logical_paths(version):
        matching_files = set()
        for content_file in content_files:
            if inventory.matches_logical_path(logical_path, content_file, version):
                matching_files.add(content_file)
        if matching_files:
            logical_path_map[logical_path] = matching_files
            
    return logical_path_map