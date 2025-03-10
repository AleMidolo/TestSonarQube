import os

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
    if not os.path.exists(path):
        return "Path does not exist"
    
    if os.path.isfile(path):
        return "file"
    
    namaste_files = [f for f in os.listdir(path) if f.startswith("0=")]
    
    if not namaste_files:
        return "No Namaste file found"
    
    namaste_file = namaste_files[0]
    with open(os.path.join(path, namaste_file), 'r') as f:
        content = f.read().strip()
    
    if content == "ocfl_1.0":
        return "root"
    elif content == "ocfl_object_1.0":
        return "object"
    else:
        return f"Unknown Namaste content: {content}"