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
    for file in manifest_files:
        with open(file, 'r') as f:
            for line in f:
                if line.startswith("digest:"):
                    digest = line.split(":")[1].strip()
                    all_digests.add(digest)
    
    # जांचें कि सभी डाइजेस्ट्स मौजूद हैं और उपयोग हो रहे हैं
    return all_digests.issubset(digests_used)