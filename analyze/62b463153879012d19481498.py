def files_list(path):
    """
    Return the files in `path`
    """
    import os
    
    # Get list of all files and directories in path
    files = os.listdir(path)
    
    # Filter to only include files (not directories)
    files = [f for f in files if os.path.isfile(os.path.join(path, f))]
    
    return files