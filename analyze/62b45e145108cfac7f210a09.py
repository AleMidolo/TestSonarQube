def check_digests_present_and_used(self, manifest_files, digests_used):
    """
    मैनिफेस्ट में सभी आवश्यक डाइजेस्ट्स की जांच करें कि वे मौजूद हैं और उपयोग हो रहे हैं।
    
    :param manifest_files: मैनिफेस्ट फाइलों की सूची
    :param digests_used: उपयोग किए गए डाइजेस्ट्स की सूची
    :return: True यदि सभी डाइजेस्ट्स मौजूद हैं और उपयोग हो रहे हैं, अन्यथा False
    """
    for manifest in manifest_files:
        with open(manifest, 'r') as file:
            content = file.read()
            for digest in digests_used:
                if digest not in content:
                    return False
    return True