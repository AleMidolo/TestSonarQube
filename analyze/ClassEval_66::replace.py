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
        num = int(match.group(1))
        return chr(num)
    return re.sub('&#(\\d+);', replace_entity, string)