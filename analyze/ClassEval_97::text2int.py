def text2int(self, textnum):
    """
        Convert the word string to the corresponding integer string
        :param textnum: string, the word string to be converted
        :return: string, the final converted integer string
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
    if textnum in self.ordinal_words:
        return str(self.ordinal_words[textnum])
    textnum = textnum.replace('-', ' ')
    words = textnum.lower().split()
    processed_words = []
    for word in words:
        if word in self.ordinal_words:
            processed_words.append(str(self.ordinal_words[word]))
            continue
        found = False
        for ending, replacement in self.ordinal_endings:
            if word.endswith(ending):
                base_word = word[:-len(ending)] + replacement
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
        elif word in self.numwords:
            scale, increment = self.numwords[word]
            current = current * scale + increment
            if scale > 100:
                result += current
                current = 0
        elif word == 'and':
            continue
    result += current
    return str(result)