def strip_root(path, root):
    if not path.startswith(root):
        raise ValueError("The path does not start with the specified root.")
    return path[len(root):]