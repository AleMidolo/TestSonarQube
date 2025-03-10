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
    manifest_digests = set()
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            for line in file:
                if "digest" in line:
                    digest = line.split(":")[1].strip()
                    manifest_digests.add(digest)
    
    # Check if all required digests are present in the manifest
    if not digests_used.issubset(manifest_digests):
        return False
    
    # Check if all digests in the manifest are being used
    if not manifest_digests.issubset(digests_used):
        return False
    
    return True