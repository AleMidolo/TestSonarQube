import os

def _eval_file(prefix, file_path):
    """
    पैकेज के फ़ाइल प्रकार की पहचान करें: `asset` या `rendition`।

    पैकेज के फ़ाइल प्रकार की पहचान करें और `packages` को फ़ाइल के प्रकार और पते के साथ अपडेट करें जो विश्लेषण में है।

    पैरामीटर्स
    ----------
    prefix : str
        XML फ़ाइल का नाम बिना एक्सटेंशन के
    file_path : str
        फ़ाइल का पूरा पथ

    रिटर्न्स
    -------
    dict
        फ़ाइल प्रकार और फ़ाइल पथ के साथ एक डिक्शनरी
    """
    file_type = None
    file_name = os.path.basename(file_path)
    
    # Check if the file is an asset or rendition based on the prefix
    if prefix in file_name:
        if "asset" in file_name.lower():
            file_type = "asset"
        elif "rendition" in file_name.lower():
            file_type = "rendition"
    
    return {
        "file_type": file_type,
        "file_path": file_path
    }