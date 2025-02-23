import os

def files_list(path):
    """
    Devuelve los archivos en `path`.
    """
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]