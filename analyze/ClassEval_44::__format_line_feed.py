def __format_line_feed(self, text):
    """
        用单个换行符替换连续的换行符
        :param text: 包含连续换行符的字符串
        :return: string, 替换后的文本，包含单个换行符
        """
    if text is None:
        return ''
    return re.sub('\\s*\\n\\s*', '\n', text).strip()