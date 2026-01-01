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
            textnum = textnum.replace(ordinal, self.units[value])
    for ending, replacement in self.ordinal_endings:
        if textnum.endswith(ending):
            textnum = '%s%s' % (textnum[:-len(ending)], replacement)
    words = textnum.lower().split()
    words = [word for word in words if word != 'and']
    current = 0
    result = 0
    for word in words:
        if word not in self.numwords:
            raise ValueError(f'Invalid word: {word}')
        scale, increment = self.numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0
    result += current
    return str(result)