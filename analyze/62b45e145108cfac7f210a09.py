def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifique que todos los resúmenes necesarios en el manifiesto estén presentes y se utilicen.
    """
    # Create sets for comparison
    manifest_digests = set()
    used_digests = set(digests_used)
    
    # Extract all digests from manifest files
    for manifest in manifest_files:
        if 'digest' in manifest:
            manifest_digests.add(manifest['digest'])
            
    # Check if all manifest digests are used
    unused_digests = manifest_digests - used_digests
    if unused_digests:
        raise ValueError(f"Found unused digests in manifest: {unused_digests}")
        
    # Check if all used digests are in manifest
    missing_digests = used_digests - manifest_digests
    if missing_digests:
        raise ValueError(f"Used digests not found in manifest: {missing_digests}")
        
    return True