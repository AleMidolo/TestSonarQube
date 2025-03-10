def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Check all digests in manifest that are needed are present and used.
    """
    # Assuming manifest_files is a list of dictionaries with 'digest' keys
    # and digests_used is a set of digests that are required
    manifest_digests = {file['digest'] for file in manifest_files}
    
    # Check if all required digests are present in the manifest
    missing_digests = digests_used - manifest_digests
    if missing_digests:
        raise ValueError(f"Missing digests: {missing_digests}")
    
    # Check if all digests in the manifest are used
    unused_digests = manifest_digests - digests_used
    if unused_digests:
        raise ValueError(f"Unused digests: {unused_digests}")
    
    return True