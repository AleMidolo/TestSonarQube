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
            processed_words.append(str(self.ordinal_words[word]))
            continue
        else:
            for ending, replacement in self.ordinal_endings:
                if word.endswith(ending):
                    word = '%s%s' % (word[:-len(ending)], replacement)
                    break
        processed_words.append(word)
    current = 0
    result = 0
    scale_stack = []
    for word in processed_words:
        if word.isdigit():
            current += int(word)
        elif word == 'and':
            continue
        elif word not in self.numwords:
            continue
        else:
            scale, increment = self.numwords[word]
            if scale > 100:
                if current == 0:
                    current = 1
                result += current * scale
                current = 0
            else:
                current = current * scale + increment
                if scale > current:
                    current = scale + increment
    result += current
    return str(result)