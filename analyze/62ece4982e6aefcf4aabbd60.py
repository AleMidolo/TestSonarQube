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
        'B': 1,
        'K': 1000,
        'M': 1000000,
        'G': 1000000000,
        'T': 1000000000000,
    }
    
    if size[-1] in multipliers:
        number = float(size[:-1])
        unit = size[-1]
    else:
        number = float(size)
        unit = 'B'
    
    return int(number * multipliers[unit])