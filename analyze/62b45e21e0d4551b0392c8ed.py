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
        # Check for OCFL Storage Root
        if any(file.startswith("0=") for file in os.listdir(path)):
            return 'root'
        
        # Check for OCFL Object
        if any(file.endswith('.json') for file in os.listdir(path)):
            return 'object'
        
        return "Directory does not match OCFL criteria"

    elif os.path.isfile(path):
        return 'file'
    
    return "Unknown path type"