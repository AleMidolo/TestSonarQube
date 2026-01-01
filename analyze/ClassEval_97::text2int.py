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
        raise ValueError('Invalid input')
    textnum = textnum.replace('-', ' ')
    current = 0
    result = 0
    for word in textnum.split():
        if word in self.numwords:
            scale, increment = self.numwords[word]
            current += increment
            if scale > 1:
                current *= scale
                result += current
                current = 0
    return str(result + current)