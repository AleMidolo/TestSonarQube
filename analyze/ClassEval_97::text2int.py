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
        return None
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
            if scale > 1:
                current = max(1, current)
                current *= scale
                if scale > 100:
                    result += current
                    current = 0
            else:
                current += increment
    result += current
    return str(result)