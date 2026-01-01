def text2int(self, textnum):
    """
        Convert the word string to the corresponding integer string
        :param textnum: string, the word string to be converted
        :return: string, the final converted integer string
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
            raise ValueError(f"Word '{word}' not recognized")
    return str(result + current)