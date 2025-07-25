def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Check all digests in manifest that are needed are present and used.
    """
    # Create a set of all digests present in the manifest files
    digests_present = set()
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            for line in file:
                if line.strip():  # Skip empty lines
                    digest = line.strip().split()[0]  # Assuming the digest is the first element
                    digests_present.add(digest)
    
    # Check if all digests used are present in the manifest
    for digest in digests_used:
        if digest not in digests_present:
            return False
    
    # Check if all digests present are used
    for digest in digests_present:
        if digest not in digests_used:
            return False
    
    return True