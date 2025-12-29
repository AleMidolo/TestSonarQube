def __format_line_feed(self, text):
    """
        Replace consecutive line breaks with a single line break
        :param text: string with consecutive line breaks
        :return:string, replaced text with single line break
        """
    if text is None:
        return ''
    text = re.sub('\\r\\n|\\n\\r|\\r', '\n', text)
    text = re.sub('\\n{2,}', '\n', text)
    return text