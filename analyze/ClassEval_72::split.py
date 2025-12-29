def split(self, pattern, text):
    """
    Dividi il testo in base ai patterns di espressione regolare e restituisci un elenco di sottostringhe
    :param pattern: stringa, Modello di espressione regolare
    :param text: stringa, Testo da dividere
    :return: elenco di stringhe, Elenco di sottostringhe dopo la divisione
    >>> ru = RegexUtils()
    >>> ru.split(r'\x08\\d{3}-\\d{3}-\\d{4}\x08', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    ['', ' abiguygusu ', ' kjgufwycs ', '']
    """
    return re.split(pattern, text)