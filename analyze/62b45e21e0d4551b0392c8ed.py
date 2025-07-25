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
        else:
            return "Not a valid OCFL Storage Root"

    elif os.path.isfile(path):
        # Check if it's a file
        if path.endswith('.json') or path.endswith('.txt'):
            return 'file'
        else:
            return "Not a valid file type"

    return "Unknown path type"