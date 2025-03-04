def list_of_file_names(settings_dirs, spec_option):
    """
    Crear un nuevo tipo complejo IniType

    Crea un nuevo tipo complejo "IniType".
    """
    file_names = []
    
    # Iterate through each directory in settings_dirs
    for directory in settings_dirs:
        # Check if spec_option is a string
        if isinstance(spec_option, str):
            # Add the file name with .ini extension
            file_names.append(f"{directory}/{spec_option}.ini")
        # If spec_option is a list/tuple
        elif isinstance(spec_option, (list, tuple)):
            # Add each option as a separate file name
            for option in spec_option:
                file_names.append(f"{directory}/{option}.ini")
                
    return file_names