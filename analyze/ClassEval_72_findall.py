import re

def findall(self, pattern, text):
    """
    Trova tutte le sottostringhe corrispondenti e restituisce un elenco di tutte le sottostringhe corrispondenti
    :param pattern: stringa, Modello di espressione regolare
    :param text: stringa, Testo da abbinare
    :return: elenco di stringhe, Elenco di tutte le sottostringhe corrispondenti
    >>> ru = RegexUtils()
    >>> ru.findall(r'\b\d{3}-\d{3}-\d{4}\b', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
    ['123-456-7890', '876-286-9876', '987-762-9767']
    """
    return re.findall(pattern, text)