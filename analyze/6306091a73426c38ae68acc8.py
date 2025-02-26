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
                    file_names.extend(files)
                except FileNotFoundError:
                    continue
            return file_names

    ini_instance = IniType(settings_dirs, spec_option)
    return ini_instance.get_file_names()