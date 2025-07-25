def list_of_file_names(settings_dirs, spec_option):
    """
    Crea un nuovo tipo complesso IniType
    """
    ini_files = []
    for directory in settings_dirs:
        for file in os.listdir(directory):
            if file.endswith('.ini') and spec_option in file:
                ini_files.append(file)
    return ini_files