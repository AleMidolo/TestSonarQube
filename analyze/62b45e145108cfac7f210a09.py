def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifica che tutti i digest nel manifesto necessari siano presenti e utilizzati.
    """
    required_digests = set()
    
    # Collect all required digests from the manifest files
    for manifest in manifest_files:
        with open(manifest, 'r') as file:
            for line in file:
                digest = line.strip()
                if digest:
                    required_digests.add(digest)
    
    # Check if all required digests are used
    missing_digests = required_digests - set(digests_used)
    
    if missing_digests:
        return False, missing_digests
    return True, None