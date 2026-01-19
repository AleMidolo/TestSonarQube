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
    pattern = '(?<!Mr)(?<!Mrs)(?<!Dr)(?<!Prof)(?<!Sr)(?<!Jr)\\.\\s|\\?\\s'
    parts = re.split(f'({pattern})', sentences_string)
    sentences = []
    current_sentence = ''
    for i in range(0, len(parts), 2):
        if i < len(parts):
            current_sentence += parts[i]
            if i + 1 < len(parts):
                delimiter = parts[i + 1]
                current_sentence += delimiter.rstrip()
                sentences.append(current_sentence.strip())
                current_sentence = ''
    if current_sentence:
        sentences.append(current_sentence.strip())
    sentences = [s for s in sentences if s]
    return sentences