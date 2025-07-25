def make_find_paths(find_paths):
    result = []
    for path in find_paths:
        # Skip patterns that already have a prefix (e.g. pp:, sh:)
        if ':' in path:
            result.append(path)
        else:
            # Transform file/path fragment into glob pattern
            # Wrap with **/* and */** to match anywhere in path
            glob_pattern = f"sh:**/*{path}*/**"
            result.append(glob_pattern)
    return result