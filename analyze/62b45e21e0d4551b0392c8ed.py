def find_path_type(path):
    """
    दिए गए पथ पर मौजूद वस्तु के प्रकार को इंगित करने वाला एक स्ट्रिंग लौटाता है।

    लौटाए जाने वाले मान:
        'root' - ऐसा लगता है कि यह OCFL स्टोरेज रूट है
        'object' - ऐसा लगता है कि यह OCFL ऑब्जेक्ट है
        'file' - यह एक फ़ाइल है, जो शायद एक इन्वेंटरी हो सकती है
        अन्य स्ट्रिंग - त्रुटि विवरण को समझाती है

    यह केवल "0=*" नमस्ते फ़ाइलों को देखकर निर्देशिका के प्रकार का निर्धारण करता है।
    """
    import os

    if not os.path.exists(path):
        return "Path does not exist"

    if os.path.isdir(path):
        if any(file.startswith("0=") for file in os.listdir(path)):
            return 'root'
        else:
            return 'object'
    
    if os.path.isfile(path):
        return 'file'
    
    return "Unknown type"