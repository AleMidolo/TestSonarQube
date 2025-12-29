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
    pattern = '(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)(?<!Prof)(?<!Sr)(?<!Jr)\\.\\s+|\\?\\s+'
    sentences = re.split(pattern, sentences_string)
    sentences = [s.strip() for s in sentences if s.strip()]
    result = []
    for i, sentence in enumerate(sentences):
        if i < len(sentences) - 1:
            start_pos = sentences_string.find(sentence)
            if start_pos != -1:
                end_pos = start_pos + len(sentence)
                if end_pos < len(sentences_string):
                    if sentences_string[end_pos:end_pos + 2] == '. ':
                        result.append(sentence + '.')
                    elif sentences_string[end_pos:end_pos + 2] == '? ':
                        result.append(sentence + '?')
                    else:
                        result.append(sentence)
        elif sentences_string.strip().endswith('.') or sentences_string.strip().endswith('?'):
            if sentences_string.strip().endswith('.'):
                result.append(sentence + '.')
            else:
                result.append(sentence + '?')
        else:
            result.append(sentence)
    return result