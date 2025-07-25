def validate_fixity(self, fixity, manifest_files):
    """
    इन्वेंटरी में फिक्सिटी ब्लॉक को सत्यापित करें।
    फिक्सिटी ब्लॉक की संरचना की जांच करें और सुनिश्चित करें कि केवल वे फाइलें
    जो मैनिफेस्ट में सूचीबद्ध हैं, वही संदर्भित की गई हैं।
    """
    # Check if fixity block is a dictionary
    if not isinstance(fixity, dict):
        return False
        
    # Check if all required keys exist in fixity block
    required_keys = ['message_digest_algorithm', 'message_digests']
    if not all(key in fixity for key in required_keys):
        return False
        
    # Check if message_digests is a list
    if not isinstance(fixity['message_digests'], list):
        return False
        
    # Check each message digest entry
    for digest in fixity['message_digests']:
        # Verify digest structure
        if not isinstance(digest, dict):
            return False
            
        if 'file_path' not in digest or 'hash' not in digest:
            return False
            
        # Verify file exists in manifest
        if digest['file_path'] not in manifest_files:
            return False
            
        # Verify hash is a string
        if not isinstance(digest['hash'], str):
            return False
            
    return True