def __format_line_feed(self, text):
    """
        Sostituisce i ritorni a capo consecutivi con un singolo ritorno a capo
        :param text: stringa con ritorni a capo consecutivi
        :return: stringa, testo sostituito con un singolo ritorno a capo
        """
    if text is None:
        return ''
    formatted_text = re.sub('\\n+', '\n', text)
    return formatted_text.strip()