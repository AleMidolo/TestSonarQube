def replace(self, string):
    """
    Reemplaza las referencias de caracteres numéricos (entidades HTML) en la cadena de entrada por sus correspondientes caracteres Unicode.
    :param string: str, la cadena de entrada que contiene referencias de caracteres numéricos.
    :return: str, la cadena de entrada con las referencias de caracteres numéricos reemplazadas por sus correspondientes caracteres Unicode.
    >>> unescaper = NumericEntityUnescaper()
    >>> unescaper.replace("&#65;&#66;&#67;")
    'ABC'

    """
    import re
    
    def replace_entity(match):
        entity = match.group(0)
        # Remove &#, &#x, or &# prefix and ; suffix
        if entity.startswith('&#x') or entity.startswith('&#X'):
            # Hexadecimal entity
            num_str = entity[3:-1]
            code_point = int(num_str, 16)
        elif entity.startswith('&#'):
            # Decimal entity
            num_str = entity[2:-1]
            code_point = int(num_str, 10)
        else:
            return entity
        
        try:
            return chr(code_point)
        except (ValueError, OverflowError):
            return entity
    
    # Pattern to match both decimal (&#123;) and hexadecimal (&#x7B; or &#X7B;) entities
    pattern = r'&#[xX]?[0-9a-fA-F]+;'
    result = re.sub(pattern, replace_entity, string)
    
    return result