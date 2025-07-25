def select_filenames_by_prefix(prefix, files):
    selected_files = []
    
    for file in files:
        # Get just the filename without path
        filename = file.split('/')[-1]
        
        # Check if filename starts with prefix
        if filename.startswith(prefix):
            selected_files.append(file)
            
    return selected_files