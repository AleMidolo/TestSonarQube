def list_of_file_names(settings_dirs, spec_option):
    class IniType:
        def __init__(self, file_names):
            self.file_names = file_names

    file_names = []
    for dir in settings_dirs:
        # Assuming we have a function that lists files in a directory based on spec_option
        files = list_files_in_directory(dir, spec_option)
        file_names.extend(files)

    return IniType(file_names)

def list_files_in_directory(directory, spec_option):
    # Placeholder for actual file listing logic based on spec_option
    import os
    return [f for f in os.listdir(directory) if f.endswith(spec_option)]