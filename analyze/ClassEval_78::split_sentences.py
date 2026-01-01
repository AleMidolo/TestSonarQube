def split_sentences(self, sentences_string):
    """
        एक स्ट्रिंग को वाक्यों की सूची में विभाजित करें। वाक्य . या ? के साथ समाप्त होते हैं और उसके बाद एक स्पेस होता है। कृपया ध्यान दें कि Mr. भी . के साथ समाप्त होता है लेकिन ये वाक्य नहीं हैं।
        :param sentences_string: स्ट्रिंग, विभाजित करने के लिए स्ट्रिंग
        :return: सूची, विभाजित वाक्य सूची
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    if not sentences_string:
        return []
    abbreviations = ['Mr', 'Mrs', 'Dr', 'Ms', 'Prof', 'St', 'Jr', 'Sr']
    placeholder_map = {}
    for i, abbr in enumerate(abbreviations):
        pattern = f'{abbr}\\.'
        placeholder = f'__ABBR{i}__'
        placeholder_map[placeholder] = f'{abbr}.'
        sentences_string = re.sub(pattern, placeholder, sentences_string)
    sentences = re.split('(?<=[.?])\\s+', sentences_string.strip())
    result = []
    for sentence in sentences:
        for placeholder, original in placeholder_map.items():
            sentence = sentence.replace(placeholder, original)
        result.append(sentence)
    return result