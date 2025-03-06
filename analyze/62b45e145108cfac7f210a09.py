def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Check all digests in manifest that are needed are present and used.
    
    Args:
        manifest_files (list): List of manifest files containing digests.
        digests_used (set): Set of digests that are used.
    
    Returns:
        bool: True if all required digests are present and used, False otherwise.
    """
    # Extract all digests from manifest files
    manifest_digests = set()
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            for line in file:
                # Assuming each line in the manifest file contains a digest
                manifest_digests.add(line.strip())
    
    # Check if all digests in the manifest are used
    if manifest_digests.issubset(digests_used):
        return True
    else:
        return False