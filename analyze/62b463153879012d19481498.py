import os

def files_list(path):
    """
    `path` में फ़ाइलों को वापस करें।
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"The path '{path}' does not exist.")
    
    if not os.path.isdir(path):
        raise NotADirectoryError(f"'{path}' is not a directory.")
    
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]