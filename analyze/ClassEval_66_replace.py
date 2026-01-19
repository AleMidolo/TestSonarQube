def replace(self, string):
    """
    Replaces numeric character references (HTML entities) in the input string with their corresponding Unicode characters.
    :param string: str, the input string containing numeric character references.
    :return: str, the input string with numeric character references replaced with their corresponding Unicode characters.
    >>> unescaper = NumericEntityUnescaper()
    >>> unescaper.replace("&#65;&#66;&#67;")
    'ABC'

    """
    import re
    
    def replace_entity(match):
        entity = match.group(0)
        # Check if it's hexadecimal (&#xHHHH; or &#XHHHH;)
        if entity[2] in ('x', 'X'):
            code_point = int(entity[3:-1], 16)
        else:
            # Decimal (&#DDDD;)
            code_point = int(entity[2:-1], 10)
        
        try:
            return chr(code_point)
        except (ValueError, OverflowError):
            # If invalid code point, return original entity
            return entity
    
    # Pattern matches &#DDDD; (decimal) or &#xHHHH; or &#XHHHH; (hexadecimal)
    pattern = r'&#[xX]?[0-9a-fA-F]+;'
    result = re.sub(pattern, replace_entity, string)
    
    return result