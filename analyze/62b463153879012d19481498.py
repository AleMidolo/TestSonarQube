import os

def files_list(path):
    """
    `path` में फ़ाइलों को वापस करें।
    """
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]