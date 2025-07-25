def files_list(path):
    """
    Devuelve los archivos en `path`.
    """
    import os
    
    # Get list of all files in directory
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(file)
            
    return files