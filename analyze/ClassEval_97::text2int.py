class Words2Numbers: 
    def __init__(self):
        """
        Initialize the word lists and dictionaries required for conversion
        """
        self.numwords = {}
        self.units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]
        self.tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        self.scales = ["hundred", "thousand", "million", "billion", "trillion"]

        self.numwords["and"] = (1, 0)
        for idx, word in enumerate(self.units):
            self.numwords[word] = (1, idx)
        for idx, word in enumerate(self.tens):
            self.numwords[word] = (1, idx * 10)
        for idx, word in enumerate(self.scales):
            self.numwords[word] = (10 ** (idx * 3 or 2), 0)

        self.ordinal_words = {'first': 1, 'second': 2, 'third': 3, 'fifth': 5, 'eighth': 8, 'ninth': 9, 'twelfth': 12}
        self.ordinal_endings = [('ieth', 'y'), ('th', '')]

    def is_valid_input(self, textnum):
        """
        Check if the input text contains only valid words that can be converted into numbers.
        :param textnum: The input text containing words representing numbers.
        :return: True if input is valid, False otherwise.
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
        textnum = textnum.replace('-', ' ')
    
        for word in textnum.split():
            if word in self.ordinal_words:
                continue
            else:
                for ending, replacement in self.ordinal_endings:
                    if word.endswith(ending):
                        word = "%s%s" % (word[:-len(ending)], replacement)
    
                if word not in self.numwords:
                    return False
    
        return True

    def text2int(self, textnum):
        """
        शब्द स्ट्रिंग को संबंधित पूर्णांक स्ट्रिंग में परिवर्तित करें
        :param textnum: स्ट्रिंग, परिवर्तित करने के लिए शब्द स्ट्रिंग
        :return: स्ट्रिंग, अंतिम परिवर्तित पूर्णांक स्ट्रिंग
        >>> w2n = Words2Numbers()
        >>> w2n.text2int("thirty-two")
        "32"
        """
        if not self.is_valid_input(textnum):
            raise ValueError("Invalid input")
        
        textnum = textnum.replace('-', ' ')
        current = 0
        total = 0
        for word in textnum.split():
            if word in self.numwords:
                scale, increment = self.numwords[word]
                current += increment
                if scale > 1:
                    total += current * scale
                    current = 0
            elif word in self.ordinal_words:
                total += self.ordinal_words[word]
                current = 0
        
        return str(total + current)