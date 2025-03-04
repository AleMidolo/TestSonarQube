def select_filenames_by_prefix(prefix, files):
    import os
    
    # Create empty list to store matching files
    matching_files = []
    
    # Loop through each file path
    for file in files:
        # Get the basename of the file
        basename = os.path.basename(file)
        
        # Check if basename starts with prefix
        if basename.startswith(prefix):
            matching_files.append(file)
            
    return matching_files