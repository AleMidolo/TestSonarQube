def list_of_file_names(settings_dirs, spec_option):
    """
    Crea un nuovo tipo complesso IniType
    """
    class IniType:
        def __init__(self, settings_dirs, spec_option):
            self.settings_dirs = settings_dirs
            self.spec_option = spec_option
            self.file_names = self._generate_file_names()

        def _generate_file_names(self):
            file_names = []
            for directory in self.settings_dirs:
                # Assuming spec_option is a filter for file types
                file_names.extend([f for f in os.listdir(directory) if f.endswith(self.spec_option)])
            return file_names

    return IniType(settings_dirs, spec_option)