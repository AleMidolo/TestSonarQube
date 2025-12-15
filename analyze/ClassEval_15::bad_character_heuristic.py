class BoyerMooreSearch: 
    def __init__(self, text, pattern):
        """
        Initializes the BoyerMooreSearch class with the given text and pattern.
        :param text: The text to be searched, str.
        :param pattern: The pattern to be searched for, str.
        """
        self.text, self.pattern = text, pattern
        self.textLen, self.patLen = len(text), len(pattern)

    def match_in_pattern(self, char):
        """
        Finds the rightmost occurrence of a character in the pattern.
        :param char: The character to be searched for, str.
        :return: The index of the rightmost occurrence of the character in the pattern, int.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.match_in_pattern("A")
        0
        """
        for i in range(self.patLen - 1, -1, -1):
            if char == self.pattern[i]:
                return i
        return -1
    
    def mismatch_in_text(self, currentPos):
        """
        Determines the position of the first dismatch between the pattern and the text.
        :param currentPos: The current position in the text, int.
        :return: The position of the first dismatch between the pattern and the text, int, otherwise -1.
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        >>> boyerMooreSearch.mismatch_in_text(0)
        2
        """
        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] != self.text[currentPos + i]:
                return currentPos + i
        return -1
    
    def bad_character_heuristic(self):
        """
        पाठ में पैटर्न की सभी उपस्थिति को खोजता है।
        :return: पाठ में पैटर्न के सभी स्थानों की एक सूची, सूची।
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        >>> boyerMooreSearch.bad_character_heuristic()
        [0, 3]
        """
        occurrences = []
        skip = 0
        
        while skip <= self.textLen - self.patLen:
            mismatch_index = self.mismatch_in_text(skip)
            if mismatch_index == -1:
                occurrences.append(skip)
                skip += 1
            else:
                char = self.text[mismatch_index]
                shift = self.match_in_pattern(char)
                if shift == -1:
                    skip += mismatch_index + 1
                else:
                    skip += mismatch_index - shift
        return occurrences