def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifique que todos los resúmenes necesarios en el manifiesto estén presentes y se utilicen.
    """
    # Extract all digests from the manifest files
    manifest_digests = set()
    for file in manifest_files:
        with open(file, 'r') as f:
            for line in f:
                if 'digest' in line:
                    manifest_digests.add(line.strip().split()[-1])
    
    # Check if all digests in the manifest are used
    for digest in manifest_digests:
        if digest not in digests_used:
            return False
    
    # Check if all used digests are in the manifest
    for digest in digests_used:
        if digest not in manifest_digests:
            return False
    
    return True