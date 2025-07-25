def make_find_paths(find_paths):
    result = []
    for path in find_paths:
        # Skip paths that already have glob patterns
        if any(c in path for c in '*?[]'):
            result.append(path)
            continue
            
        # Skip paths with special prefixes like pp:
        if ':' in path:
            result.append(path)
            continue
            
        # Convert normal paths to glob pattern
        # Add **/* prefix and */** suffix to match file anywhere in directory tree
        glob_path = f'sh:**/*{path}*/**'
        result.append(glob_path)
        
    return tuple(result)