def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Check all digests in manifest that are needed are present and used.
    """
    # Create a set of digests from the manifest files
    manifest_digests = set()
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            for line in file:
                if line.strip():  # Skip empty lines
                    digest = line.strip().split()[0]  # Assuming the digest is the first element
                    manifest_digests.add(digest)
    
    # Check if all digests in manifest are used
    missing_digests = manifest_digests - digests_used
    if missing_digests:
        raise ValueError(f"Some digests in the manifest are not used: {missing_digests}")
    
    # Check if all used digests are present in the manifest
    extra_digests = digests_used - manifest_digests
    if extra_digests:
        raise ValueError(f"Some used digests are not present in the manifest: {extra_digests}")
    
    return True