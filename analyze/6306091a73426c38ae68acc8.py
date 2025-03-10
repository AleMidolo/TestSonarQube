def list_of_file_names(settings_dirs, spec_option):
    """
    Crea un nuovo tipo complesso IniType
    """
    # Implementation goes here
    file_names = []
    for directory in settings_dirs:
        # Assuming spec_option is a filter or pattern to match file names
        # This is a placeholder for actual file filtering logic
        if spec_option in directory:
            file_names.append(directory)
    return file_names