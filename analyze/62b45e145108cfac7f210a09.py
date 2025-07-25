def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    मैनिफेस्ट में सभी आवश्यक डाइजेस्ट्स की जांच करें कि वे मौजूद हैं और उपयोग हो रहे हैं।
    
    Args:
        manifest_files (list): मैनिफेस्ट फाइलों की सूची।
        digests_used (list): उपयोग किए गए डाइजेस्ट्स की सूची।
    
    Returns:
        bool: True अगर सभी डाइजेस्ट्स मौजूद हैं और उपयोग हो रहे हैं, अन्यथा False।
    """
    # सभी डाइजेस्ट्स की जांच करें कि वे मैनिफेस्ट में मौजूद हैं
    for digest in digests_used:
        if digest not in manifest_files:
            return False
    
    # सभी डाइजेस्ट्स की जांच करें कि वे उपयोग हो रहे हैं
    for digest in manifest_files:
        if digest not in digests_used:
            return False
    
    return True