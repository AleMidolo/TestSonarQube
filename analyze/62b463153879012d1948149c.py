def select_filenames_by_prefix(prefix, files):
    import os
    
    # Initialize empty list to store matching files
    matching_files = []
    
    # Iterate through all files
    for file in files:
        # Get basename of file
        basename = os.path.basename(file)
        
        # Check if basename starts with prefix
        if basename.startswith(prefix):
            matching_files.append(file)
            
    return matching_files