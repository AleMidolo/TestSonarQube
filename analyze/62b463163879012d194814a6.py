def files_list_from_zipfile(zip_path):
    """
    Restituisce i file presenti in `zip_path`.
    
    Args:
        zip_path (str): Path to the zip file
        
    Returns:
        list: List of files in the zip archive
    """
    import zipfile
    
    files = []
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        files = zip_ref.namelist()
    
    return files