def was_processed(processed, path_name, verbose):
    """
    Check if the given path_name has already been processed.

    Args:
        processed (set): A set containing the paths that have already been processed.
        path_name (str): The path to check if it has been processed.
        verbose (bool): If True, print additional information.

    Returns:
        bool: True if the path_name has been processed, False otherwise.
    """
    if path_name in processed:
        if verbose:
            print(f"{path_name} has already been processed.")
        return True
    else:
        if verbose:
            print(f"{path_name} has not been processed yet.")
        return False