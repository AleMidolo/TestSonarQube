def files_list_from_zipfile(zip_path):
    """
    `zip_path` में फ़ाइलें लौटाएँ
    """
    import zipfile
    
    files_list = []
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Get list of all files in zip
        files_list = zip_ref.namelist()
        
        # Sort the list alphabetically
        files_list.sort()
        
    return files_list