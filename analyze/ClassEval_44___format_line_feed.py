def __format_line_feed(text):
    """
    Sostituisce i ritorni a capo consecutivi con un singolo ritorno a capo
    :param text: stringa con ritorni a capo consecutivi
    :return: stringa, testo sostituito con un singolo ritorno a capo
    """
    import re
    return re.sub(r'\n+', '\n', text)