def split_sentences(self, sentences_string):
    """
        Split a string into a list of sentences. Sentences end with . or ? and with a space after that. Please note that Mr. also end with . but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    abbreviations = ['Mr', 'Mrs', 'Ms', 'Dr', 'Prof', 'St', 'Jr', 'Sr']
    placeholder_map = {}
    for i, abbr in enumerate(abbreviations):
        pattern = f'\\b{abbr}\\.'
        placeholder = f'__ABBR{i}__'
        sentences_string = re.sub(pattern, placeholder, sentences_string)
        placeholder_map[placeholder] = f'{abbr}.'
    sentences = re.split('(?<=[.?])\\s+', sentences_string.strip())
    result = []
    for sentence in sentences:
        for placeholder, original in placeholder_map.items():
            sentence = sentence.replace(placeholder, original)
        result.append(sentence)
    return result