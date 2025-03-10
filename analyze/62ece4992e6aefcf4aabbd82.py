import re

def get_pattern(pattern, strip=True):
    """
    Questo metodo converte la stringa fornita in un oggetto pattern regex.
    
    :param pattern: La stringa da convertire in un pattern regex.
    :param strip: Se True, rimuove gli spazi bianchi all'inizio e alla fine della stringa.
    :return: Un oggetto regex pattern compilato.
    """
    if strip:
        pattern = pattern.strip()
    return re.compile(pattern)