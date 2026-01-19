import re

def sub(self, pattern, replacement, text):
    """
    Sostituisce la sottostringa corrispondente a un'espressione regolare con la stringa specificata
    :param pattern: stringa, Modello di espressione regolare
    :param replacement: Testo con cui sostituire
    :param text: stringa, Testo da sostituire
    :return: stringa, Testo dopo la sostituzione
    >>> ru = RegexUtils()
    >>> ru.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'phone num',  "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    'phone num abiguygusu phone num kjgufwycs phone num'
    """
    return re.sub(pattern, replacement, text)