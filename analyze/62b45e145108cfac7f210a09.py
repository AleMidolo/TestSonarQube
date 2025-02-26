def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Check all digests in manifest that are needed are present and used.
    """
    missing_digests = []
    used_digests = set(digests_used)

    for manifest in manifest_files:
        for digest in manifest.get('digests', []):
            if digest not in used_digests:
                missing_digests.append(digest)

    return missing_digests