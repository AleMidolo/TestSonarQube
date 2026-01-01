def text2int(self, textnum):
    """
        Convertire la stringa di parole nel corrispondente numero intero
        :param textnum: stringa, la stringa di parole da convertire
        :return: stringa, la stringa finale convertita in numero intero
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
    if not self.is_valid_input(textnum):
        return textnum
    current = 0
    result = 0
    textnum = textnum.lower().replace('-', ' ')
    words = textnum.split()
    for word in words:
        if word in self.ordinal_words:
            current += self.ordinal_words[word]
        else:
            for ending, replacement in self.ordinal_endings:
                if word.endswith(ending):
                    word = '%s%s' % (word[:-len(ending)], replacement)
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