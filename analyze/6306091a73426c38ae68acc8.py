def list_of_file_names(settings_dirs, spec_option):
    """
    Crea un nuovo tipo complesso IniType
    """
    class IniType:
        def __init__(self, directory, option):
            self.directory = directory
            self.option = option

        def __repr__(self):
            return f"IniType(directory={self.directory}, option={self.option})"

    ini_types = []
    for directory in settings_dirs:
        ini_type = IniType(directory, spec_option)
        ini_types.append(ini_type)

    return ini_types