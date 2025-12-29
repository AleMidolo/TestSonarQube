def text2int(self, textnum):
    """
        शब्द स्ट्रिंग को संबंधित पूर्णांक स्ट्रिंग में परिवर्तित करें
        :param textnum: स्ट्रिंग, परिवर्तित करने के लिए शब्द स्ट्रिंग
        :return: स्ट्रिंग, अंतिम परिवर्तित पूर्णांक स्ट्रिंग
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
    if not self.is_valid_input(textnum):
        raise ValueError('Invalid input')
    textnum = textnum.replace('-', ' ')
    current = 0
    total = 0
    for word in textnum.split():
        if word in self.numwords:
            scale, increment = self.numwords[word]
            current += increment
            if scale > 1:
                total += current * scale
                current = 0
        elif word in self.ordinal_words:
            total += self.ordinal_words[word]
            current = 0
    return str(total + current)