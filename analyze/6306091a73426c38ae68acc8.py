def list_of_file_names(settings_dirs, spec_option):
    """
    एक नया IniType कॉम्प्लेक्स टाइप बनाएं
    """
    import os
    file_names = []
    for directory in settings_dirs:
        if os.path.exists(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if spec_option in file:
                        file_names.append(os.path.join(root, file))
    return file_names