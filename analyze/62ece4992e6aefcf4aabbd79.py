def make_find_paths(find_paths):
    result = []
    for path in find_paths:
        # Skip if it's already a pattern (contains :)
        if ':' in path:
            result.append(path)
            continue
            
        # Convert regular path to glob pattern
        # Add ** before and after to match anywhere in path
        # Add * before and after filename to match partial names
        filename = path.split('/')[-1]
        pattern = f"sh:**/*{filename}*/**"
        result.append(pattern)
        
    return result