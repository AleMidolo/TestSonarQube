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
    size = size.upper()
    if size[-1] == 'K':
        return int(size[:-1]) * 1000
    elif size[-1] == 'M':
        return int(size[:-1]) * 1000 * 1000
    elif size[-1] == 'G':
        return int(size[:-1]) * 1000 * 1000 * 1000
    elif size[-1] == 'T':
        return int(size[:-1]) * 1000 * 1000 * 1000 * 1000
    else:
        return int(size)