def get_logical_path_map(inventory, version):
    logical_path_map = {}
    
    # Iterate through all versions up to and including target version
    for v in range(version + 1):
        if v in inventory:
            # For each file in this version
            for logical_path, content_file in inventory[v].items():
                # Initialize set if logical path not seen before
                if logical_path not in logical_path_map:
                    logical_path_map[logical_path] = set()
                
                # Add content file to set for this logical path
                logical_path_map[logical_path].add(content_file)
                
    return logical_path_map