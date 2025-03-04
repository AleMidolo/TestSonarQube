def files_list_from_zipfile(zip_path):
    """
    返回给定压缩文件路径中的文件列表。

    返回 `zip_path` 中的文件。
    """
    import zipfile
    
    files_list = []
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Get list of files in zip archive
        files_list = zip_ref.namelist()
        
    return files_list