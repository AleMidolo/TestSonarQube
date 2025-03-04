def make_find_paths(find_paths):
    transformed_paths = []
    
    for path in find_paths:
        # Skip patterns that already have a prefix (e.g. pp:)
        if ':' in path:
            transformed_paths.append(path)
            continue
            
        # Transform regular paths into glob patterns
        # Add **/* prefix and */** suffix to match files anywhere in directory tree
        # that contain the original filename
        glob_pattern = f"sh:**/*{path}*/**"
        transformed_paths.append(glob_pattern)
        
    return transformed_paths