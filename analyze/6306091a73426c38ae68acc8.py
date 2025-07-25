def list_of_file_names(settings_dirs, spec_option):
    """
    Crea un nuovo tipo complesso IniType
    """
    file_names = []
    for directory in settings_dirs:
        if spec_option in directory:
            file_names.append(directory)
    return file_names