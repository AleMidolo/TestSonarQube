def text2int(self, textnum):
    """
        शब्द स्ट्रिंग को संबंधित पूर्णांक स्ट्रिंग में परिवर्तित करें
        :param textnum: स्ट्रिंग, परिवर्तित करने के लिए शब्द स्ट्रिंग
        :return: स्ट्रिंग, अंतिम परिवर्तित पूर्णांक स्ट्रिंग
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
    textnum = textnum.replace('-', ' ')
    for ordinal, value in self.ordinal_words.items():
        if ordinal in textnum:
            textnum = textnum.replace(ordinal, str(value))
    for ending, replacement in self.ordinal_endings:
        if textnum.endswith(ending):
            textnum = '%s%s' % (textnum[:-len(ending)], replacement)
    current = 0
    result = 0
    words = textnum.lower().split()
    for word in words:
        if word == 'and':
            continue
        if word not in self.numwords:
            found = False
            for ending, replacement in self.ordinal_endings:
                if word.endswith(ending):
                    base_word = '%s%s' % (word[:-len(ending)], replacement)
                    if base_word in self.numwords:
                        word = base_word
                        found = True
                        break
            if not found:
                continue
        scale, increment = self.numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0
    result += current
    return str(result)