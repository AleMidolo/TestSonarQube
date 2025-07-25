def size_to_bytes(size: str) -> int:
    """
    मानव-पठनीय फ़ाइल आकार को बाइट्स में परिवर्तित करें।

    परिणामी मान एक अनुमान है क्योंकि इनपुट मान अधिकांश मामलों में राउंड किया गया होता है।

    तर्क (Args):
        आकार (size): एक स्ट्रिंग जो मानव-पठनीय फ़ाइल आकार का प्रतिनिधित्व करती है (उदा: '500K')

    रिटर्न (Returns):
        फ़ाइल आकार का दशमलव (decimal) प्रतिनिधित्व

    उदाहरण (Examples)::

        >>> size_to_bytes("500")
        500
        >>> size_to_bytes("1K")
        1000
    """
    size = size.strip().upper()
    multipliers = {
        'K': 1000,
        'M': 1000**2,
        'G': 1000**3,
        'T': 1000**4,
        'P': 1000**5,
        'E': 1000**6,
    }
    
    if size.isdigit():
        return int(size)
    
    for suffix, multiplier in multipliers.items():
        if size.endswith(suffix):
            return int(float(size[:-1]) * multiplier)
    
    raise ValueError("Invalid size format")