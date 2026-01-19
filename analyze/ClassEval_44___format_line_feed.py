def __format_line_feed(self, text):
    """
        Reemplaza los saltos de línea consecutivos por un solo salto de línea
        :param text: cadena con saltos de línea consecutivos
        :return: cadena, texto reemplazado con un solo salto de línea
        """
    if text is None:
        return ''
    formatted_text = re.sub('\\n+', '\n', text)
    return formatted_text.strip()