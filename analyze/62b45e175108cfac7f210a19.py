def validate_fixity(self, fixity, manifest_files):
    """
    Validate fixity block in inventory.

    Check the structure of the fixity block and makes sure that only files
    listed in the manifest are referenced.
    """
    if not isinstance(fixity, dict):
        raise ValueError("Fixity must be a dictionary.")

    if not isinstance(manifest_files, list):
        raise ValueError("Manifest files must be a list.")

    for file in fixity.get('files', []):
        if file not in manifest_files:
            raise ValueError(f"File {file} in fixity is not in the manifest.")

    required_keys = {'files', 'checksum_type', 'checksum_value'}
    if not required_keys.issubset(fixity.keys()):
        raise ValueError("Fixity block is missing required keys.")
    
    return True