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
        raise ValueError('Invalid input')
    textnum = textnum.replace('-', ' ')
    current = result = 0
    for word in textnum.split():
        if word in self.numwords:
            scale, increment = self.numwords[word]
            current += increment
            if scale > 1:
                current *= scale
                result += current
                current = 0
        else:
            raise ValueError(f"Word '{word}' is not recognized.")
    return str(result + current)