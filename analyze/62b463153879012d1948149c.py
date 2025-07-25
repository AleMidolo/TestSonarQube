def select_filenames_by_prefix(prefix, files):
    """
    Get files which belongs to a document package.

    Retorna os arquivos da lista `files` cujos nomes iniciam com `prefix`

    Parameters
    ----------
    prefix : str
        Filename prefix
    files : str list
        Files paths
    Returns
    -------
    list
        files paths which basename files matches to prefix
    """
    import os
    
    matching_files = []
    
    for file_path in files:
        # Get just the filename without directory path
        basename = os.path.basename(file_path)
        
        # Check if filename starts with prefix
        if basename.startswith(prefix):
            matching_files.append(file_path)
            
    return matching_files