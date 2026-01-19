def replace(self, string):
    """
    Sostituisce i riferimenti ai caratteri numerici (entità HTML) nella stringa di input con i loro corrispondenti caratteri Unicode.
    :param string: str, la stringa di input contenente riferimenti ai caratteri numerici.
    :return: str, la stringa di input con i riferimenti ai caratteri numerici sostituiti con i loro corrispondenti caratteri Unicode.
    >>> unescaper = NumericEntityUnescaper()
    >>> unescaper.replace("&#65;&#66;&#67;")
    'ABC'

    """
    import re
    
    def replace_entity(match):
        entity = match.group(0)
        # Remove &#, &#x or &# prefix and ; suffix
        if entity.startswith('&#x') or entity.startswith('&#X'):
            # Hexadecimal entity
            num_str = entity[3:-1]
            char_code = int(num_str, 16)
        elif entity.startswith('&#'):
            # Decimal entity
            num_str = entity[2:-1]
            char_code = int(num_str, 10)
        else:
            return entity
        
        return chr(char_code)
    
    # Pattern to match numeric entities: &#digits; or &#xhexdigits;
    pattern = r'&#[xX]?[0-9a-fA-F]+;'
    result = re.sub(pattern, replace_entity, string)
    
    return result