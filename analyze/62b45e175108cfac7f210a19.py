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
        
    # Check each message digest entry
    for digest in fixity['message_digests']:
        # Each entry should be a dict
        if not isinstance(digest, dict):
            return False
            
        # Should have required fields
        if not all(key in digest for key in ['file_path', 'hash']):
            return False
            
        # Fields should be strings
        if not isinstance(digest['file_path'], str) or not isinstance(digest['hash'], str):
            return False
            
        # File path should exist in manifest files
        if digest['file_path'] not in manifest_files:
            return False
            
    return True