def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    Check all digests in manifest that are needed are present and used.
    """
    missing_digests = []
    unused_digests = []

    for manifest in manifest_files:
        for digest in manifest.get('digests', []):
            if digest not in digests_used:
                unused_digests.append(digest)

    for digest in digests_used:
        if digest not in [d for manifest in manifest_files for d in manifest.get('digests', [])]:
            missing_digests.append(digest)

    return {
        'missing_digests': missing_digests,
        'unused_digests': unused_digests
    }