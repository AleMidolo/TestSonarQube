def replace(self, string):
    """
    इनपुट स्ट्रिंग में संख्या वर्ण संदर्भ (HTML संस्थाएँ) को उनके संबंधित यूनिकोड वर्णों के साथ बदलता है।
    :param string: str, इनपुट स्ट्रिंग जिसमें संख्या वर्ण संदर्भ शामिल हैं।
    :return: str, इनपुट स्ट्रिंग जिसमें संख्या वर्ण संदर्भ को उनके संबंधित यूनिकोड वर्णों के साथ बदला गया है।
    >>> unescaper = NumericEntityUnescaper()
    >>> unescaper.replace("&#65;&#66;&#67;")
    'ABC'

    """
    import re
    
    def replace_entity(match):
        entity = match.group(0)
        # Check if it's hexadecimal (&#xHHHH;) or decimal (&#DDDD;)
        if entity[2] in 'xX':
            # Hexadecimal format
            num = int(entity[3:-1], 16)
        else:
            # Decimal format
            num = int(entity[2:-1], 10)
        return chr(num)
    
    # Pattern to match both decimal (&#65;) and hexadecimal (&#x41;) numeric character references
    pattern = r'&#[xX]?[0-9a-fA-F]+;'
    result = re.sub(pattern, replace_entity, string)
    
    return result