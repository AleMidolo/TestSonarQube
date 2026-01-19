def match(self, pattern, text):
    """
    Controlla se il testo corrisponde all'espressione regolare
    :param pattern: stringa, Modello di espressione regolare
    :param text: stringa, Testo da abbinare
    :return: True o False, che rappresenta se il testo corrisponde o meno all'espressione regolare
    >>> ru = RegexUtils()
    >>> ru.match(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890")
    True
    """
    import re
    return bool(re.search(pattern, text))