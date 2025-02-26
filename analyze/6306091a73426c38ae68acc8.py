def list_of_file_names(settings_dirs, spec_option):
    """
    # Crear un nuevo tipo complejo IniType

    Crea un nuevo tipo complejo "IniType".
    """
    class IniType:
        def __init__(self, settings_dirs, spec_option):
            self.settings_dirs = settings_dirs
            self.spec_option = spec_option

        def get_file_names(self):
            file_names = []
            for directory in self.settings_dirs:
                try:
                    files = os.listdir(directory)
                    for file in files:
                        if self.spec_option in file:
                            file_names.append(file)
                except FileNotFoundError:
                    continue
            return file_names

    return IniType(settings_dirs, spec_option)