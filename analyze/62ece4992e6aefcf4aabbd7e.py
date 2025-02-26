def _resolve_string(matcher):
    """
    पर्यावरण से मान प्राप्त करें, जिसमें एक मैचर होता है जो एक नाम और वैकल्पिक डिफ़ॉल्ट मान को शामिल करता है।  
    यदि पर्यावरण में चर परिभाषित नहीं है और कोई डिफ़ॉल्ट मान प्रदान नहीं किया गया है, तो एक त्रुटि उत्पन्न की जाती है।
    """
    import os

    name = matcher.get('name')
    default_value = matcher.get('default')

    value = os.environ.get(name)

    if value is None:
        if default_value is not None:
            return default_value
        else:
            raise ValueError(f"Environment variable '{name}' is not defined and no default value provided.")

    return value