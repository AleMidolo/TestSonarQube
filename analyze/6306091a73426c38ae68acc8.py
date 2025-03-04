def list_of_file_names(settings_dirs, spec_option):
    """
    Crea un nuovo tipo complesso IniType
    """
    file_names = []
    
    # Iterate through each directory path
    for directory in settings_dirs:
        # Check if directory exists and is a directory
        if os.path.isdir(directory):
            # Get list of files in directory
            files = os.listdir(directory)
            
            # Filter files based on spec_option
            for file in files:
                if spec_option in file and file.endswith('.ini'):
                    # Add full path to file_names list
                    file_names.append(os.path.join(directory, file))
                    
    return file_names