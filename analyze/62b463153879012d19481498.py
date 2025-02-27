import os

def files_list(path):
    """
    Restituisce i file nel percorso `path`.
    """
    try:
        return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    except FileNotFoundError:
        return []
    except PermissionError:
        return []