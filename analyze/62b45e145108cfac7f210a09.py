def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Verifique que todos los resúmenes necesarios en el manifiesto estén presentes y se utilicen.
    """
    manifest_digests = set()
    for file in manifest_files:
        with open(file, 'r') as f:
            for line in f:
                if line.strip():
                    manifest_digests.add(line.strip())
    
    digests_used_set = set(digests_used)
    
    missing_digests = manifest_digests - digests_used_set
    unused_digests = digests_used_set - manifest_digests
    
    if missing_digests:
        raise ValueError(f"Missing digests: {missing_digests}")
    if unused_digests:
        raise ValueError(f"Unused digests: {unused_digests}")
    
    return True