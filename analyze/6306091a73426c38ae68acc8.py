def list_of_file_names(settings_dirs, spec_option):
    """
    एक नया IniType कॉम्प्लेक्स टाइप बनाएं
    """
    file_names = []
    
    # Iterate through each directory path in settings_dirs
    for dir_path in settings_dirs:
        # Check if spec_option is a string
        if isinstance(spec_option, str):
            # Add the file name with .ini extension
            file_names.append(f"{spec_option}.ini")
        # If spec_option is a list/tuple
        elif isinstance(spec_option, (list, tuple)):
            # Add each option with .ini extension
            for option in spec_option:
                file_names.append(f"{option}.ini")
                
    return file_names