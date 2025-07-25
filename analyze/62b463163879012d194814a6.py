def files_list_from_zipfile(zip_path):
    """
    Devuelve los archivos en `zip_path`.
    
    Args:
        zip_path: Path al archivo zip
        
    Returns:
        list: Lista de nombres de archivos contenidos en el zip
    """
    import zipfile
    
    files_list = []
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        files_list = zip_ref.namelist()
        
    return files_list