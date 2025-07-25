def _explore_zipfile(zip_path):
    """
    Get packages' data from zip_path

    Groups files by their XML basename and returns data in dict format.

    Parameters
    ----------
    zip_path : str
        zip file path
    Returns
    -------
    dict
    """
    import zipfile
    from collections import defaultdict
    
    # Dictionary to store grouped files
    grouped_files = defaultdict(dict)
    
    # Open and read zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Get list of all files in zip
        file_list = zip_ref.namelist()
        
        # Group files by their XML basename
        for filename in file_list:
            # Skip directories
            if filename.endswith('/'):
                continue
                
            # Get base name without extension
            base_name = filename.split('/')[-1].rsplit('.', 1)[0]
            
            # Get file extension
            extension = filename.split('.')[-1].lower()
            
            # Read file content
            with zip_ref.open(filename) as f:
                content = f.read()
                
            # Store content in grouped_files dictionary
            grouped_files[base_name][extension] = content
            
    return dict(grouped_files)