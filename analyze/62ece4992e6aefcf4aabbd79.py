def make_find_paths(find_paths):
    transformed_paths = []
    for path in find_paths:
        if ':' in path or '*' in path or '?' in path or '[' in path or ']' in path:
            transformed_paths.append(path)
        else:
            transformed_paths.append(f'sh:**/*{path}*/**')
    return tuple(transformed_paths)