def __format_line_feed(self, text):
    """
        Reemplaza los saltos de línea consecutivos por un solo salto de línea
        :param text: cadena con saltos de línea consecutivos
        :return: cadena, texto reemplazado con un solo salto de línea
        """
    if not text:
        return text
    return re.sub('\\n{2,}', '\n', text)