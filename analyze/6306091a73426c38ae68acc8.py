def list_of_file_names(settings_dirs, spec_option):
    """
    एक नया IniType कॉम्प्लेक्स टाइप बनाएं
    """
    import os
    
    file_names = []
    
    for directory in settings_dirs:
        if os.path.exists(directory):
            for file in os.listdir(directory):
                if spec_option in file:
                    file_names.append(file)
    
    return file_names