def list_of_file_names(settings_dirs, spec_option):
    """
    Crea un nuovo tipo complesso IniType
    """
    file_names = []
    
    # Iterate through each directory path
    for directory in settings_dirs:
        # Check if directory path ends with /
        if not directory.endswith('/'):
            directory += '/'
            
        # Create full file path by combining directory and spec_option
        file_path = directory + spec_option
        
        # Add file path to list
        file_names.append(file_path)
        
    return file_names