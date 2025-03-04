def was_processed(processed, path_name, verbose):
    """
    Check if a file or directory has already been processed.

    To prevent recursion, expand the path name to an absolution path
    call this function with a set that will store all the entries and
    the entry to test. If the entry is already in the set, report the issue
    and return ``True``. Otherwise, add the entry to the set and return
    ``False`` to allow the path to be processed.

    Args:
        processed: Set to store processed pathnames
        path_name: Path to a directory or file
        verbose: True if verbose output is requested

    Returns:
        True if it's already in the set. False if not.
    """
    # Convert path to absolute path
    abs_path = os.path.abspath(path_name)
    
    # Check if path has already been processed
    if abs_path in processed:
        if verbose:
            print(f"Already processed {abs_path}")
        return True
        
    # Add path to processed set
    processed.add(abs_path)
    return False