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
        # Handle spec option cases
        if spec_option.endswith('*'):
            # Get all files matching pattern
            base = spec_option[:-1]
            for file in os.listdir(directory):
                if file.startswith(base):
                    file_names.append(os.path.join(directory, file))
        else:
            # Get specific file
            file_path = os.path.join(directory, spec_option)
            if os.path.exists(file_path):
                file_names.append(file_path)
                
    return file_names