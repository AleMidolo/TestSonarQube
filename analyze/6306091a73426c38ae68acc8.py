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
        # Handle different spec options
        if spec_option == 'ini':
            file_names.extend([f for f in os.listdir(directory) if f.endswith('.ini')])
        elif spec_option == 'conf':
            file_names.extend([f for f in os.listdir(directory) if f.endswith('.conf')])
        elif spec_option == 'all':
            file_names.extend([f for f in os.listdir(directory) if f.endswith(('.ini', '.conf'))])
            
    # Remove duplicates while preserving order
    return list(dict.fromkeys(file_names))