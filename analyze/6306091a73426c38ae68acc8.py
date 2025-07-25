def list_of_file_names(settings_dirs, spec_option):
    """
    Create a new IniType complex type
    """
    import os

    class IniType:
        def __init__(self, name, path):
            self.name = name
            self.path = path

    ini_files = []
    for directory in settings_dirs:
        for file in os.listdir(directory):
            if file.endswith('.ini') and (spec_option in file):
                ini_files.append(IniType(file, os.path.join(directory, file)))

    return ini_files