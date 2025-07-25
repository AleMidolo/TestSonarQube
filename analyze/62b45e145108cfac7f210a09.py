def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifica che tutti i digest nel manifesto necessari siano presenti e utilizzati.
    """
    # Get all digests from manifest files
    manifest_digests = set()
    for manifest in manifest_files:
        if 'digest' in manifest:
            manifest_digests.add(manifest['digest'])
            
    # Get all digests that were actually used
    used_digests = set(digests_used)
    
    # Check that all manifest digests were used
    unused_digests = manifest_digests - used_digests
    if unused_digests:
        raise ValueError(f"Found unused digests in manifest: {unused_digests}")
        
    # Check that all used digests are in manifest
    missing_digests = used_digests - manifest_digests
    if missing_digests:
        raise ValueError(f"Used digests not found in manifest: {missing_digests}")
        
    return True