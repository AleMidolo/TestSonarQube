def list_of_file_names(settings_dirs, spec_option):
    """
    एक नया IniType कॉम्प्लेक्स टाइप बनाएं
    """
    file_names = []
    
    # Iterate through each directory in settings_dirs
    for directory in settings_dirs:
        # Check if spec_option is a string or list
        if isinstance(spec_option, str):
            # Add single file name
            file_names.append(f"{directory}/{spec_option}")
        elif isinstance(spec_option, list):
            # Add multiple file names
            for option in spec_option:
                file_names.append(f"{directory}/{option}")
                
    return file_names