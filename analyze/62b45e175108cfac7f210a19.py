def validate_fixity(self, fixity, manifest_files):
    """
    Validate fixity block in inventory.

    Check the structure of the fixity block and makes sure that only files
    listed in the manifest are referenced.
    """
    # Check if fixity is a dictionary
    if not isinstance(fixity, dict):
        raise ValueError("Fixity must be a dictionary.")

    # Check if manifest_files is a set for faster lookup
    manifest_set = set(manifest_files)

    # Validate each file in the fixity block
    for file, checksum in fixity.items():
        if not isinstance(file, str) or not isinstance(checksum, str):
            raise ValueError(f"Invalid entry in fixity: {file}: {checksum}")
        if file not in manifest_set:
            raise ValueError(f"File {file} in fixity is not listed in the manifest.")

    return True