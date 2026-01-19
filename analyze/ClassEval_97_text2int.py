def text2int(self, textnum):
    """
        Convert the word string to the corresponding integer string
        :param textnum: string, the word string to be converted
        :return: string, the final converted integer string
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
    textnum = textnum.replace('-', ' ')
    words = textnum.split()
    processed_words = []
    for word in words:
        if word in self.ordinal_words:
            processed_words.append(self.units[self.ordinal_words[word]])
        else:
            for ending, replacement in self.ordinal_endings:
                if word.endswith(ending):
                    word = '%s%s' % (word[:-len(ending)], replacement)
            processed_words.append(word)
    words = processed_words
    current = 0
    result = 0
    for word in words:
        if word not in self.numwords:
            continue
        scale, increment = self.numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0
    result += current
    return str(result)