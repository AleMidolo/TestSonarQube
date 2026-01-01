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
    matches = list(re.finditer(pattern, sentences_string))
    result = []
    for i, sentence in enumerate(sentences):
        if i < len(matches):
            punct_match = matches[i].group()
            punct = punct_match[0]
            result.append(sentence + punct)
        elif sentence.endswith('.') or sentence.endswith('?'):
            result.append(sentence)
        else:
            result.append(sentence)
    return result