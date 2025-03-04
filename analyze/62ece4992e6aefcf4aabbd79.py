def make_find_paths(find_paths):
    transformed_paths = []
    
    for path in find_paths:
        # Check if path is already a pattern (contains pp:)
        if path.startswith('pp:'):
            transformed_paths.append(path)
        else:
            # Transform regular path fragment into glob pattern
            # Add **/* prefix and */** suffix to match file anywhere in directory tree
            transformed = f'sh:**/*{path}*/**'
            transformed_paths.append(transformed)
            
    return transformed_paths