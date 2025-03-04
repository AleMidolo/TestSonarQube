def files_list_from_zipfile(zip_path):
    """
    Restituisce i file presenti in `zip_path`.
    
    Args:
        zip_path: Path del file zip
        
    Returns:
        list: Lista dei file contenuti nel file zip
    """
    import zipfile
    
    files = []
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        files = zip_ref.namelist()
    
    return files