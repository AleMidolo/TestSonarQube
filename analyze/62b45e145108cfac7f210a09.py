def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    मैनिफेस्ट में सभी आवश्यक डाइजेस्ट्स की जांच करें कि वे मौजूद हैं और उपयोग हो रहे हैं।
    
    Args:
        manifest_files (list): A list of manifest files to check.
        digests_used (set): A set of digests that are expected to be present and used.
    
    Returns:
        bool: True if all digests are present and used, False otherwise.
    """
    # Extract all digests from the manifest files
    digests_in_manifest = set()
    for manifest in manifest_files:
        with open(manifest, 'r') as file:
            for line in file:
                if "digest" in line:  # Assuming digests are marked with "digest" in the manifest
                    digest = line.split(":")[1].strip()
                    digests_in_manifest.add(digest)
    
    # Check if all required digests are present in the manifest
    if not digests_used.issubset(digests_in_manifest):
        return False
    
    # Check if all digests in the manifest are being used
    if not digests_in_manifest.issubset(digests_used):
        return False
    
    return True