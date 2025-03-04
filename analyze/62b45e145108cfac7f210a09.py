def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifica che tutti i digest nel manifesto necessari siano presenti e utilizzati.
    """
    required_digests = set()
    
    # Collect all required digests from the manifest files
    for manifest in manifest_files:
        with open(manifest, 'r') as file:
            data = file.read()
            # Assuming the digest is represented in a specific format, e.g., as lines
            required_digests.update(data.splitlines())
    
    # Check if all required digests are present in the used digests
    missing_digests = required_digests - set(digests_used)
    
    if missing_digests:
        raise ValueError(f"Missing digests: {missing_digests}")
    
    return True