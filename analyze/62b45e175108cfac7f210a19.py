def validate_fixity(self, fixity, manifest_files):
    """
    इन्वेंटरी में फिक्सिटी ब्लॉक को सत्यापित करें।
    फिक्सिटी ब्लॉक की संरचना की जांच करें और सुनिश्चित करें कि केवल वे फाइलें
    जो मैनिफेस्ट में सूचीबद्ध हैं, वही संदर्भित की गई हैं।
    """
    # Check if fixity block is a dictionary
    if not isinstance(fixity, dict):
        return False
        
    # Check that all required keys exist
    required_keys = ['message_digest_algorithm', 'message_digests']
    if not all(key in fixity for key in required_keys):
        return False
        
    # Check message digest algorithm is string
    if not isinstance(fixity['message_digest_algorithm'], str):
        return False
        
    # Check message digests is list
    if not isinstance(fixity['message_digests'], list):
        return False
        
    # Get all filenames referenced in fixity block
    fixity_files = set()
    for digest in fixity['message_digests']:
        if not isinstance(digest, dict):
            return False
        if 'filepath' not in digest or 'message_digest' not in digest:
            return False
        fixity_files.add(digest['filepath'])
        
    # Convert manifest files to set for comparison
    manifest_files = set(manifest_files)
    
    # Check that all files in fixity block are in manifest
    if not fixity_files.issubset(manifest_files):
        return False
        
    return True