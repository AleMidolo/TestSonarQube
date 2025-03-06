def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Check all digests in manifest that are needed are present and used.
    """
    # Extract all digests from the manifest files
    manifest_digests = set()
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            for line in file:
                if 'digest' in line:
                    digest = line.split('digest:')[1].strip()
                    manifest_digests.add(digest)
    
    # Check if all required digests are present in the manifest
    missing_digests = set(digests_used) - manifest_digests
    if missing_digests:
        raise ValueError(f"Missing digests in manifest: {missing_digests}")
    
    # Check if all manifest digests are used
    unused_digests = manifest_digests - set(digests_used)
    if unused_digests:
        raise ValueError(f"Unused digests in manifest: {unused_digests}")
    
    return True