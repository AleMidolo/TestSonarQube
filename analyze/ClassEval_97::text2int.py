def text2int(self, textnum):
    """
        शब्द स्ट्रिंग को संबंधित पूर्णांक स्ट्रिंग में परिवर्तित करें
        :param textnum: स्ट्रिंग, परिवर्तित करने के लिए शब्द स्ट्रिंग
        :return: स्ट्रिंग, अंतिम परिवर्तित पूर्णांक स्ट्रिंग
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
    textnum = textnum.lower().replace('-', ' ')
    words = textnum.split()
    current = 0
    result = 0
    for word in words:
        if word in self.ordinal_words:
            current += self.ordinal_words[word]
        else:
            for ending, replacement in self.ordinal_endings:
                if word.endswith(ending):
                    word = word[:-len(ending)] + replacement
                    break
            if word not in self.numwords:
                continue
            scale, increment = self.numwords[word]
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
    result += current
    return str(result)