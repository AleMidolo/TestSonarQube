def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifique que todos los resúmenes necesarios en el manifiesto estén presentes y se utilicen.
    """
    # Extract all digests from the manifest files
    manifest_digests = set()
    for manifest in manifest_files:
        manifest_digests.update(manifest.get('digests', []))
    
    # Check if all required digests are present in the manifest
    missing_digests = set(digests_used) - manifest_digests
    if missing_digests:
        raise ValueError(f"Missing digests in manifest: {missing_digests}")
    
    # Check if all manifest digests are used
    unused_digests = manifest_digests - set(digests_used)
    if unused_digests:
        raise ValueError(f"Unused digests in manifest: {unused_digests}")
    
    return True