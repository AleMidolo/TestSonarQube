import os

def _resolve_string(matcher):
    """
    पर्यावरण से मान प्राप्त करें, जिसमें एक मैचर होता है जो एक नाम और वैकल्पिक डिफ़ॉल्ट मान को शामिल करता है।  
    यदि पर्यावरण में चर परिभाषित नहीं है और कोई डिफ़ॉल्ट मान प्रदान नहीं किया गया है, तो एक त्रुटि उत्पन्न की जाती है।
    """
    name, *default = matcher.groups()
    value = os.getenv(name)
    
    if value is not None:
        return value
    elif default:
        return default[0]
    else:
        raise ValueError(f"Environment variable '{name}' is not defined and no default value is provided.")