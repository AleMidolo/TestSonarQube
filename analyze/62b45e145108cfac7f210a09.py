def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    मैनिफेस्ट में सभी आवश्यक डाइजेस्ट्स की जांच करें कि वे मौजूद हैं और उपयोग हो रहे हैं।
    
    :param manifest_files: मैनिफेस्ट फाइलों की सूची
    :param digests_used: उपयोग किए गए डाइजेस्ट्स की सूची
    :return: सभी डाइजेस्ट्स मौजूद और उपयोग हो रहे हैं तो True, अन्यथा False
    """
    for digest in digests_used:
        if digest not in manifest_files:
            return False
    return True