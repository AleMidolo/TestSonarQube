def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    मैनिफेस्ट में सभी आवश्यक डाइजेस्ट्स की जांच करें कि वे मौजूद हैं और उपयोग हो रहे हैं।
    """
    missing_digests = []
    used_digests = set(digests_used)

    for manifest in manifest_files:
        for digest in manifest.get('digests', []):
            if digest in used_digests:
                used_digests.remove(digest)

    missing_digests = list(used_digests)

    return missing_digests