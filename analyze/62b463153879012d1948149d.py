def _explore_folder(folder):
    """
    Get packages' data from folder

    Groups files by their XML basename and returns data in dict format.

    Parameters
    ----------
    folder : str
        Folder of the package
    Returns
    -------
    dict
    """
    import os
    from collections import defaultdict
    
    # Dictionary to store file groups
    file_groups = defaultdict(dict)
    
    # Walk through folder
    for root, _, files in os.walk(folder):
        for file in files:
            # Get full file path
            file_path = os.path.join(root, file)
            
            # Get file extension
            _, ext = os.path.splitext(file)
            
            # Get base filename without extension
            base_name = os.path.splitext(file)[0]
            
            # Group files by base name
            if ext.lower() in ['.xml', '.pdf', '.txt']:
                file_groups[base_name][ext.lower()] = file_path
    
    # Convert defaultdict to regular dict
    return dict(file_groups)