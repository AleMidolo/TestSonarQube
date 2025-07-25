def make_find_paths(find_paths):
    result = []
    for path in find_paths:
        # Skip if it's already a pattern (contains :)
        if ':' in path:
            result.append(path)
        else:
            # Convert fragment to glob pattern
            # Add ** before and after to match anywhere in path
            # Add * before and after filename to match partial names
            glob_pattern = f"sh:**/*{path}*/**"
            result.append(glob_pattern)
    return result