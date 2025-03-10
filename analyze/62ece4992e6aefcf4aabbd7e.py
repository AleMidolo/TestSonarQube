import os

def _resolve_string(matcher):
    """
    पर्यावरण से मान प्राप्त करें, जिसमें एक मैचर होता है जो एक नाम और वैकल्पिक डिफ़ॉल्ट मान को शामिल करता है।  
    यदि पर्यावरण में चर परिभाषित नहीं है और कोई डिफ़ॉल्ट मान प्रदान नहीं किया गया है, तो एक त्रुटि उत्पन्न की जाती है।
    """
    if not matcher:
        raise ValueError("Matcher cannot be empty.")
    
    parts = matcher.split(':')
    var_name = parts[0].strip()
    default_value = None if len(parts) == 1 else parts[1].strip()
    
    value = os.getenv(var_name)
    
    if value is not None:
        return value
    elif default_value is not None:
        return default_value
    else:
        raise ValueError(f"Environment variable '{var_name}' is not defined and no default value is provided.")