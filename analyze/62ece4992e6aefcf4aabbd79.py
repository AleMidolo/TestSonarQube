def make_find_paths(find_paths):
    transformed_paths = []
    
    for path in find_paths:
        # Skip patterns that already have a prefix (e.g. pp:)
        if ':' in path:
            transformed_paths.append(path)
            continue
            
        # Transform regular paths into glob patterns
        # Add **/* prefix and */** suffix to match files anywhere in directory tree
        transformed = f"sh:**/*{path}*/**"
        transformed_paths.append(transformed)
        
    return transformed_paths