def __format_line_feed(self, text):
    """
        Replace consecutive line breaks with a single line break
        :param text: string with consecutive line breaks
        :return:string, replaced text with single line break
        """
    if not text:
        return text
    return re.sub('\\n\\s*\\n', '\n', text.strip())