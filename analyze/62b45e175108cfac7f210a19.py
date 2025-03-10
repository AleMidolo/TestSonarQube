def validate_fixity(self, fixity, manifest_files):
    """
    Validate fixity block in inventory.

    Check the structure of the fixity block and makes sure that only files
    listed in the manifest are referenced.
    """
    if not isinstance(fixity, dict):
        raise ValueError("Fixity block must be a dictionary.")
    
    for file_name, checksums in fixity.items():
        if file_name not in manifest_files:
            raise ValueError(f"File '{file_name}' in fixity block is not listed in the manifest.")
        
        if not isinstance(checksums, dict):
            raise ValueError(f"Checksums for file '{file_name}' must be a dictionary.")
        
        for algorithm, checksum in checksums.items():
            if not isinstance(algorithm, str) or not isinstance(checksum, str):
                raise ValueError(f"Algorithm and checksum for file '{file_name}' must be strings.")
    
    return True