def match(filename):
    """
    Check if the filename is a type that this module supports

    Args:
        filename: Filename to match
    Returns:
        False if not a match, True if supported
    """
    supported_extensions = ['.txt', '.csv', '.json', '.xml']
    return any(filename.endswith(ext) for ext in supported_extensions)