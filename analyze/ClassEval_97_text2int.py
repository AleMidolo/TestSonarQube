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
    words = textnum.lower().split()
    processed_words = []
    for word in words:
        if word in self.ordinal_words:
            processed_words.append(str(self.ordinal_words[word]))
            continue
        else:
            found = False
            for ending, replacement in self.ordinal_endings:
                if word.endswith(ending):
                    base_word = '%s%s' % (word[:-len(ending)], replacement)
                    if base_word in self.numwords:
                        processed_words.append(base_word)
                        found = True
                        break
            if not found:
                processed_words.append(word)
    current = 0
    result = 0
    for word in processed_words:
        if word.isdigit():
            current += int(word)
        elif word not in self.numwords:
            continue
        else:
            scale, increment = self.numwords[word]
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
    result += current
    return str(result)