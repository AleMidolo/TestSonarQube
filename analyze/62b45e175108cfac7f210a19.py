def validate_fixity(self, fixity, manifest_files):
    """
    Validate fixity block in inventory.

    Check the structure of the fixity block and makes sure that only files
    listed in the manifest are referenced.

    Args:
        fixity (dict): The fixity block to validate.
        manifest_files (list): List of files in the manifest.

    Returns:
        bool: True if the fixity block is valid, False otherwise.
    """
    if not isinstance(fixity, dict):
        return False
    
    for file_name, checksums in fixity.items():
        if file_name not in manifest_files:
            return False
        
        if not isinstance(checksums, dict):
            return False
        
        for algorithm, checksum in checksums.items():
            if not isinstance(algorithm, str) or not isinstance(checksum, str):
                return False
    
    return True