def files_list(path):
    """
    Devuelve los archivos en `path`.
    """
    import os
    
    # Get list of all files and directories in path
    contents = os.listdir(path)
    
    # Filter to only include files (not directories)
    files = [f for f in contents if os.path.isfile(os.path.join(path, f))]
    
    return files