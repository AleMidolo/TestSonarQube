def split(self, pattern, text):
    """
        Divide el texto basado en patrones de expresiones regulares y devuelve una lista de subcadenas
        :param pattern: cadena, Patrón de expresión regular
        :param text: cadena, Texto a dividir
        :return: lista de cadenas, Lista de subcadenas después de dividir
        >>> ru = RegexUtils()
        >>> ru.split(r'\x08\\d{3}-\\d{3}-\\d{4}\x08', "123-456-7890 abiguygusu 876-286-9876 kjgufwycs 987-762-9767")
        ['', ' abiguygusu ', ' kjgufwycs ', '']
        """
    return re.split(pattern, text)