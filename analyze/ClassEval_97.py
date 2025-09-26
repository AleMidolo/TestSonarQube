class Words2Numbers:

    def __init__(self):
        self.numwords = {}
        self.units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]
        self.tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.scales = ["hundred", "thousand", "million", "billion", "trillion"]

        self.numwords["and"] = (1, 0)
        self._initialize_numwords()

        self.ordinal_words = {'first': 1, 'second': 2, 'third': 3, 'fifth': 5, 'eighth': 8, 'ninth': 9, 'twelfth': 12}
        self.ordinal_endings = [('ieth', 'y'), ('th', '')]

    def _initialize_numwords(self):
        for idx, word in enumerate(self.units):
            self.numwords[word] = (1, idx)
        for idx, word in enumerate(self.tens):
            self.numwords[word] = (1, idx * 10)
        for idx, word in enumerate(self.scales):
            self.numwords[word] = (10 ** (idx * 3 or 2), 0)

    def text2int(self, textnum):
        textnum = textnum.replace('-', ' ')
        current, result, curstring, onnumber = 0, 0, "", False

        for word in textnum.split():
            if word in self.ordinal_words:
                current = self._process_ordinal_word(word, current)
                onnumber = True
            else:
                word = self._replace_ordinal_ending(word)
                if word not in self.numwords:
                    curstring = self._handle_invalid_word(word, curstring, result, current, onnumber)
                    result, current, onnumber = 0, 0, False
                else:
                    current = self._process_numword(word, current)
                    if self._is_scale(word):
                        result += current
                        current = 0
                    onnumber = True

        if onnumber:
            curstring += repr(result + current)

        return curstring

    def _process_ordinal_word(self, word, current):
        scale, increment = (1, self.ordinal_words[word])
        return current * scale + increment

    def _replace_ordinal_ending(self, word):
        for ending, replacement in self.ordinal_endings:
            if word.endswith(ending):
                return "%s%s" % (word[:-len(ending)], replacement)
        return word

    def _handle_invalid_word(self, word, curstring, result, current, onnumber):
        if onnumber:
            curstring += repr(result + current) + " "
        curstring += word + " "
        return curstring

    def _process_numword(self, word, current):
        scale, increment = self.numwords[word]
        return current * scale + increment

    def _is_scale(self, word):
        return self.numwords[word][0] > 100

    def is_valid_input(self, textnum):
        textnum = textnum.replace('-', ' ')
        for word in textnum.split():
            if not self._is_valid_word(word):
                return False
        return True

    def _is_valid_word(self, word):
        if word in self.ordinal_words:
            return True
        word = self._replace_ordinal_ending(word)
        return word in self.numwords