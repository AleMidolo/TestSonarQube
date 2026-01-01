def text2int(self, textnum):
    """
        Convierte la cadena de palabras en la cadena de número entero correspondiente
        :param textnum: cadena, la cadena de palabras a ser convertida
        :return: cadena, la cadena de número entero final convertida
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
    textnum = textnum.replace('-', ' ')
    current = result = 0
    words = textnum.lower().split()
    for word in words:
        if word in self.ordinal_words:
            value = self.ordinal_words[word]
            current += value
            continue
        original_word = word
        for ending, replacement in self.ordinal_endings:
            if word.endswith(ending):
                word = '%s%s' % (word[:-len(ending)], replacement)
                break
        if word not in self.numwords:
            if original_word in self.numwords:
                word = original_word
            else:
                continue
        scale, increment = self.numwords[word]
        if scale > 1:
            current = current * scale if current != 0 else scale
            if scale > 100:
                result += current
                current = 0
        else:
            current += increment
    result += current
    return str(result)