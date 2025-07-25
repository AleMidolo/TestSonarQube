def list_of_file_names(settings_dirs, spec_option):
    """
    Create a new IniType complex type.

    Args:
        settings_dirs (list): List of directories to search for files.
        spec_option (str): Specification option to filter files.

    Returns:
        list: List of file names that match the specification.
    """
    import os
    file_names = []
    for directory in settings_dirs:
        if os.path.isdir(directory):
            for file in os.listdir(directory):
                if spec_option in file:
                    file_names.append(file)
    return file_names