def list_of_file_names(settings_dirs, spec_option):
    """
    Create a new IniType complex type
    """
    file_names = []
    
    # Handle single directory case
    if isinstance(settings_dirs, str):
        settings_dirs = [settings_dirs]
        
    # Iterate through all directories
    for directory in settings_dirs:
        # Handle spec_option file extension
        if spec_option.startswith('.'):
            pattern = f'*{spec_option}'
        else:
            pattern = f'*.{spec_option}'
            
        # Get all matching files in directory
        import glob
        import os
        
        search_path = os.path.join(directory, pattern)
        matching_files = glob.glob(search_path)
        
        # Add file names without extension to list
        for file_path in matching_files:
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            file_names.append(file_name)
            
    return sorted(list(set(file_names))) # Remove duplicates and sort