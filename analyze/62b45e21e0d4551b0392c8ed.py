import os

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
    if not os.path.exists(path):
        return "त्रुटि: पथ मौजूद नहीं है"
    
    if os.path.isfile(path):
        return "file"
    
    if os.path.isdir(path):
        # Check if it's an OCFL storage root
        if os.path.exists(os.path.join(path, "0=ocfl_1.0")):
            return "root"
        
        # Check if it's an OCFL object
        if os.path.exists(os.path.join(path, "inventory.json")):
            return "object"
        
        # Check for "0=*" files
        for filename in os.listdir(path):
            if filename.startswith("0="):
                return "object"
        
        return "त्रुटि: पथ OCFL रूट या ऑब्जेक्ट नहीं है"
    
    return "त्रुटि: अज्ञात पथ प्रकार"