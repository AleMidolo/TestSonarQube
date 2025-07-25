def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    मैनिफेस्ट में सभी आवश्यक डाइजेस्ट्स की जांच करें कि वे मौजूद हैं और उपयोग हो रहे हैं।
    
    Args:
        manifest_files (list): मैनिफेस्ट फ़ाइलों की सूची।
        digests_used (list): उपयोग किए गए डाइजेस्ट्स की सूची।
    
    Returns:
        bool: True यदि सभी डाइजेस्ट्स मौजूद हैं और उपयोग हो रहे हैं, अन्यथा False।
    """
    # मैनिफेस्ट फ़ाइलों से सभी डाइजेस्ट्स निकालें
    manifest_digests = set()
    for file in manifest_files:
        with open(file, 'r') as f:
            for line in f:
                if 'digest' in line:
                    digest = line.split('digest:')[1].strip()
                    manifest_digests.add(digest)
    
    # उपयोग किए गए डाइजेस्ट्स को सेट में बदलें
    used_digests = set(digests_used)
    
    # जांचें कि सभी उपयोग किए गए डाइजेस्ट्स मैनिफेस्ट में मौजूद हैं
    return used_digests.issubset(manifest_digests)