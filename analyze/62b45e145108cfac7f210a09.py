def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    मैनिफेस्ट में सभी आवश्यक डाइजेस्ट्स की जांच करें कि वे मौजूद हैं और उपयोग हो रहे हैं।
    """
    # Create sets of digests from manifest files and used digests
    manifest_digests = set()
    for manifest in manifest_files:
        if 'digest' in manifest:
            manifest_digests.add(manifest['digest'])
    
    digests_used = set(digests_used)
    
    # Check if all digests in manifest are being used
    unused_digests = manifest_digests - digests_used
    if unused_digests:
        raise ValueError(f"Found unused digests in manifest: {unused_digests}")
        
    # Check if all used digests exist in manifest
    missing_digests = digests_used - manifest_digests
    if missing_digests:
        raise ValueError(f"Used digests not found in manifest: {missing_digests}")
        
    return True