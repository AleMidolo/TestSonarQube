def match(self, pattern, text):
    """
        Controlla se il testo corrisponde all'espressione regolare
        :param pattern: stringa, Modello di espressione regolare
        :param text: stringa, Testo da abbinare
        :return: True o False, che rappresenta se il testo corrisponde o meno all'espressione regolare
        >>> ru = RegexUtils()
        >>> ru.match(r'\x08\\d{3}-\\d{3}-\\d{4}\x08', "123-456-7890")
        True
        """
    return re.match(pattern, text) is not None