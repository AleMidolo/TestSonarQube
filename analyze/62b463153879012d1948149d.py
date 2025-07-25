def _explore_folder(folder):
    import os
    import re
    
    # Initialize empty dictionary to store grouped files
    grouped_files = {}
    
    # Get all files in the folder
    files = os.listdir(folder)
    
    # Group files by XML filename
    for file in files:
        # Get full file path
        file_path = os.path.join(folder, file)
        
        # Skip if not a file
        if not os.path.isfile(file_path):
            continue
            
        # Extract base filename without extension
        base_name = os.path.splitext(file)[0]
        
        # Remove any suffixes like _eng, _chn etc
        base_name = re.sub(r'_[a-z]{3}$', '', base_name)
        
        # Initialize list for this base name if not exists
        if base_name not in grouped_files:
            grouped_files[base_name] = []
            
        # Add file to group
        grouped_files[base_name].append(file_path)
        
    return grouped_files