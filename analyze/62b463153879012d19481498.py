import os

def files_list(path):
    """
    Restituisce i file nel percorso `path`.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path '{path}' does not exist.")
    
    if not os.path.isdir(path):
        raise NotADirectoryError(f"'{path}' is not a directory.")
    
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]