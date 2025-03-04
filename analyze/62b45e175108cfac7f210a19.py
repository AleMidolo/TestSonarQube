def validate_fixity(self, fixity, manifest_files):
    """
    Validate fixity block in inventory.

    Check the structure of the fixity block and makes sure that only files
    listed in the manifest are referenced.
    """
    if not isinstance(fixity, dict):
        raise ValueError("Fixity block must be a dictionary")
        
    # Check each algorithm block
    for algorithm, checksums in fixity.items():
        if not isinstance(algorithm, str):
            raise ValueError("Fixity algorithm must be a string")
            
        if not isinstance(checksums, dict):
            raise ValueError(f"Checksums for {algorithm} must be a dictionary")
            
        # Validate each file checksum
        for filepath, checksum in checksums.items():
            if not isinstance(filepath, str):
                raise ValueError("File path must be a string")
                
            if not isinstance(checksum, str):
                raise ValueError("Checksum must be a string")
                
            # Check that file exists in manifest
            if filepath not in manifest_files:
                raise ValueError(f"File {filepath} in fixity block not found in manifest")
                
    return True