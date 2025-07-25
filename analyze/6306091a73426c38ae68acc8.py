def list_of_file_names(settings_dirs, spec_option):
    """
    Crea un nuevo tipo complejo "IniType".
    """
    # Implementation to create a new complex type "IniType"
    class IniType:
        def __init__(self, settings_dirs, spec_option):
            self.settings_dirs = settings_dirs
            self.spec_option = spec_option

        def __repr__(self):
            return f"IniType(settings_dirs={self.settings_dirs}, spec_option={self.spec_option})"

    return IniType(settings_dirs, spec_option)