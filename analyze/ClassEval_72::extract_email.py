def extract_email(self, text):
        """
        从文本中提取所有电子邮件地址
        :param text: 字符串，输入文本
        :return: 字符串列表，所有提取的电子邮件地址
        >>> ru = RegexUtils()
        >>> ru.extract_email("abcdefg@163.com ygusyfysy@126.com wljduyuv@qq.com")
        ['abcdefg@163.com', 'ygusyfysy@126.com', 'wljduyuv@qq.com']
        """
        pattern = self.generate_email_pattern()
        return self.findall(pattern, text)