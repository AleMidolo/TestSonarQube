def match(filename):
    """
    Check if the filename is a type that this module supports

    Args:
        filename: Filename to match
    Returns:
        False if not a match, True if supported
    """
    # List of supported file extensions
    supported_extensions = ['.txt', '.csv', '.json', '.xml', '.yaml', '.yml']
    
    # Get the file extension from the filename
    file_extension = filename[filename.rfind('.'):].lower() if '.' in filename else ''
    
    # Check if extension is in supported list
    return file_extension in supported_extensions