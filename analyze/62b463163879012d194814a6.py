def files_list_from_zipfile(zip_path):
    """
    Devuelve los archivos en `zip_path`.
    
    Args:
        zip_path (str): Path to the zip file
        
    Returns:
        list: List of file paths contained in the zip file
    """
    import zipfile
    
    files_list = []
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        files_list = zip_ref.namelist()
        
    return files_list