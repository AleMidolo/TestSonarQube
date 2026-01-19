def generate_split_sentences_pattern(self):
    """
    Genera patrones de expresiones regulares que coinciden con los caracteres intermedios de dos oraciones
    :return: cadena, patrones de expresiones regulares que coinciden con los caracteres intermedios de dos oraciones
    >>> ru = RegexUtils()
    >>> ru.generate_split_sentences_pattern()
    '[.!?][\s]{1,2}(?=[A-Z])'
    """
    return r'[.!?][\s]{1,2}(?=[A-Z])'