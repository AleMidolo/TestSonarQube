def _resolve_string(matcher):
    # मैचर से नाम और डिफ़ॉल्ट मान निकालें
    name = matcher.group(1)
    default = matcher.group(2) if matcher.lastindex > 1 else None
    
    # पर्यावरण से मान प्राप्त करें
    value = os.environ.get(name)
    
    # यदि मान नहीं मिला और डिफ़ॉल्ट मान नहीं दिया गया
    if value is None and default is None:
        raise ValueError(f"Environment variable '{name}' not found and no default value provided")
        
    # यदि मान नहीं मिला तो डिफ़ॉल्ट मान लौटाएं
    return value if value is not None else default