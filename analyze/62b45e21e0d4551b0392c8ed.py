def find_path_type(path):
    """
    Return a string indicating the type of thing at the given path.

    Return values:
        'root' - looks like an OCFL Storage Root
        'object' - looks like an OCFL Object
        'file' - a file, might be an inventory
        other string explains error description

    Looks only at "0=*" Namaste files to determine the directory type.
    """
    import os

    if not os.path.exists(path):
        return "Path does not exist"

    if os.path.isdir(path):
        namaste_files = [f for f in os.listdir(path) if f.startswith("0=")]
        if any(f.endswith('.json') for f in namaste_files):
            return 'root'
        elif any(f.endswith('.txt') for f in namaste_files):
            return 'object'
        else:
            return 'unknown directory type'
    
    elif os.path.isfile(path):
        return 'file'
    
    return 'other: not a valid path type'