def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifique que todos los resúmenes necesarios en el manifiesto estén presentes y se utilicen.
    """
    # Extract all digests from the manifest files
    manifest_digests = set()
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            for line in file:
                if 'digest' in line:
                    digest = line.split('digest:')[1].strip()
                    manifest_digests.add(digest)
    
    # Check if all digests in the manifest are used
    for digest in manifest_digests:
        if digest not in digests_used:
            return False
    
    # Check if all used digests are in the manifest
    for digest in digests_used:
        if digest not in manifest_digests:
            return False
    
    return True