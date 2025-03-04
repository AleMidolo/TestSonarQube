def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Check all digests in manifest that are needed are present and used.
    """
    # Get all digests from manifest files
    manifest_digests = set()
    for manifest in manifest_files:
        if 'digest' in manifest:
            manifest_digests.add(manifest['digest'])
            
    # Check all digests in manifest are used
    unused_digests = manifest_digests - set(digests_used)
    if unused_digests:
        raise ValueError(f"Found unused digests in manifest: {unused_digests}")
        
    # Check all used digests are in manifest
    missing_digests = set(digests_used) - manifest_digests
    if missing_digests:
        raise ValueError(f"Used digests not found in manifest: {missing_digests}")
        
    return True