def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Check all digests in manifest that are needed are present and used.
    """
    required_digests = set()
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            for line in file:
                if line.strip():
                    digest = line.split()[0]  # Assuming the digest is the first element in the line
                    required_digests.add(digest)
    
    missing_digests = required_digests - digests_used
    unused_digests = digests_used - required_digests
    
    if missing_digests:
        print(f"Missing digests: {missing_digests}")
    if unused_digests:
        print(f"Unused digests: {unused_digests}")
    
    return not missing_digests and not unused_digests