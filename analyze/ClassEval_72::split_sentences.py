def split_sentences(self, text):
        """
        Split the text into a list of sentences without Punctuation except the last sentence
        :param text: Text to be split
        :return: Split Text List
        >>> ru = RegexUtils()
        >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
        ['Aaa', 'Bbbb', 'Ccc!']
        """
        sentences = re.split(r'[.!?]', text)
        return [sentence.strip() for sentence in sentences if sentence.strip()][: -1] + [text.split('.')[-1].strip()]