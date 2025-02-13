def check_digests_present_and_used(self, manifest_files, digests_used):
    needed_digests = set()
    for manifest in manifest_files:
        with open(manifest, 'r') as file:
            for line in file:
                digest = line.strip()
                needed_digests.add(digest)

    missing_digests = needed_digests - set(digests_used)
    
    if missing_digests:
        return self.error(f"Missing digests: {', '.join(missing_digests)}")
    
    return None