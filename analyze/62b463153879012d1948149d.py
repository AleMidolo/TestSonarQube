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
            ext = ext.lower()
            
            # Get base filename without extension
            base_name = os.path.splitext(file)[0]
            
            # Group files by base name
            if ext in ['.xml', '.pdf', '.jpg', '.jpeg', '.png']:
                if ext == '.xml':
                    file_groups[base_name]['xml'] = file_path
                elif ext == '.pdf':
                    file_groups[base_name]['pdf'] = file_path
                else:  # Images
                    if 'images' not in file_groups[base_name]:
                        file_groups[base_name]['images'] = []
                    file_groups[base_name]['images'].append(file_path)
    
    return dict(file_groups)