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
    
    # Convert filename to lowercase and get extension
    if not isinstance(filename, str):
        return False
        
    filename = filename.lower()
    _, ext = os.path.splitext(filename)
    
    # Check if extension is in supported list
    return ext in supported_extensions