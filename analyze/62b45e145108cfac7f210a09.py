def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    मैनिफेस्ट में सभी आवश्यक डाइजेस्ट्स की जांच करें कि वे मौजूद हैं और उपयोग हो रहे हैं।
    
    Args:
        manifest_files (list): मैनिफेस्ट फाइलों की सूची।
        digests_used (set): उपयोग किए गए डाइजेस्ट्स का सेट।
    
    Returns:
        bool: True अगर सभी डाइजेस्ट्स मौजूद हैं और उपयोग हो रहे हैं, अन्यथा False।
    """
    # मैनिफेस्ट फाइलों से सभी डाइजेस्ट्स को इकट्ठा करें
    all_digests = set()
    for manifest_file in manifest_files:
        with open(manifest_file, 'r') as file:
            for line in file:
                if 'digest' in line:
                    digest = line.split('digest:')[1].strip()
                    all_digests.add(digest)
    
    # सभी डाइजेस्ट्स की जांच करें कि वे मौजूद हैं और उपयोग हो रहे हैं
    for digest in all_digests:
        if digest not in digests_used:
            return False
    
    return True