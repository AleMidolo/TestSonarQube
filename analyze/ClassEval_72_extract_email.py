def extract_email(self, text):
    """
        पाठ से सभी ईमेल पते निकालें
        :param text: स्ट्रिंग, इनपुट पाठ
        :return: स्ट्रिंग की सूची, सभी निकाले गए ईमेल पते
        >>> ru = RegexUtils()
        >>> ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
        ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com']
        """
    pattern = self.generate_email_pattern()
    return self.findall(pattern, text)