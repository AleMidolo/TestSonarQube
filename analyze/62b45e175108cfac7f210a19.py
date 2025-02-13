def validate_fixity(self, fixity, manifest_files):
    if not isinstance(fixity, dict):
        return self.error("Fixity block must be a dictionary.")
    
    for file in fixity.get('files', []):
        if file not in manifest_files:
            return self.error(f"File '{file}' in fixity block is not listed in the manifest.")
    
    required_keys = {'files', 'checksum_type', 'checksum_value'}
    if not required_keys.issubset(fixity.keys()):
        return self.error("Fixity block is missing required keys.")
    
    return True