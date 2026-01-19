def extract_email(self, text):
    """
        Extraer todas las direcciones de correo electrónico del texto
        :param text: cadena, texto de entrada
        :return: lista de cadenas, todas las direcciones de correo electrónico extraídas
        >>> ru = RegexUtils()
        >>> ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
        ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com']
        """
    pattern = self.generate_email_pattern()
    return self.findall(pattern, text)