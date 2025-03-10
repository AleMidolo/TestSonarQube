def list_of_file_names(settings_dirs, spec_option):
    """
    एक नया IniType कॉम्प्लेक्स टाइप बनाएं
    """
    import os
    file_names = []
    for directory in settings_dirs:
        if os.path.isdir(directory):
            for file in os.listdir(directory):
                if file.endswith(spec_option):
                    file_names.append(file)
    return file_names