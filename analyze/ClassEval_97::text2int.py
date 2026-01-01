def text2int(self, textnum):
    """
        Convierte la cadena de palabras en la cadena de número entero correspondiente
        :param textnum: cadena, la cadena de palabras a ser convertida
        :return: cadena, la cadena de número entero final convertida
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
    if not self.is_valid_input(textnum):
        raise ValueError('Invalid input: contains non-numeric words')
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