def get_logical_path_map(inventory, version):
    logical_path_map = {}
    
    for state, files in inventory.items():
        if state['version'] == version:
            for file in files:
                logical_path = file['logical_path']
                if logical_path not in logical_path_map:
                    logical_path_map[logical_path] = set()
                logical_path_map[logical_path].add(file['file_path'])
    
    return logical_path_map