def files_list(path):
    """    
    `path` में फ़ाइलों को वापस करें।
    """
    import os
    
    # Get list of files in directory
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(file)
            
    return files