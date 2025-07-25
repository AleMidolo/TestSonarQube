def list_of_file_names(settings_dirs, spec_option):
    """
    Crea un nuovo tipo complesso IniType
    """
    import os
    file_names = []
    for directory in settings_dirs:
        if os.path.isdir(directory):
            for file_name in os.listdir(directory):
                if file_name.endswith(spec_option):
                    file_names.append(os.path.join(directory, file_name))
    return file_names