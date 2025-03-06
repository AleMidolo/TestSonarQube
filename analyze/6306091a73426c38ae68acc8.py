def list_of_file_names(settings_dirs, spec_option):
    """
    Crea un nuevo tipo complejo "IniType".
    """
    class IniType:
        def __init__(self, settings_dirs, spec_option):
            self.settings_dirs = settings_dirs
            self.spec_option = spec_option

        def get_file_names(self):
            # Placeholder for the logic to list file names based on settings_dirs and spec_option
            file_names = []
            # Example logic (to be replaced with actual implementation)
            for directory in self.settings_dirs:
                # Assuming spec_option is a filter or pattern
                if self.spec_option in directory:
                    file_names.append(directory)
            return file_names

    return IniType(settings_dirs, spec_option)