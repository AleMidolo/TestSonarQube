def __format_line_feed(text):
    """
        Reemplaza los saltos de línea consecutivos por un solo salto de línea
        :param text: cadena con saltos de línea consecutivos
        :return: cadena, texto reemplazado con un solo salto de línea
        """
    return re.sub('\\n+', '\n', text).strip()