def list_of_file_names(settings_dirs, spec_option):
    """
    एक नया IniType कॉम्प्लेक्स टाइप बनाएं
    """
    file_names = []
    
    # Handle single directory or list of directories
    if isinstance(settings_dirs, str):
        settings_dirs = [settings_dirs]
        
    # Iterate through all directories
    for directory in settings_dirs:
        # Get all files in directory that match spec_option
        if spec_option.endswith('.ini'):
            # If spec_option is a specific .ini file
            if os.path.isfile(os.path.join(directory, spec_option)):
                file_names.append(os.path.join(directory, spec_option))
        else:
            # If spec_option is a pattern/prefix
            for file in os.listdir(directory):
                if file.startswith(spec_option) and file.endswith('.ini'):
                    file_names.append(os.path.join(directory, file))
                    
    return file_names