def mismatch_in_text(self, currentPos):
    """
        पैटर्न और टेक्स्ट के बीच पहले असमानता की स्थिति निर्धारित करता है।
        :param currentPos: टेक्स्ट में वर्तमान स्थिति, int.
        :return: पैटर्न और टेक्स्ट के बीच पहले असमानता की स्थिति, int, अन्यथा -1।
        >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        >>> boyerMooreSearch.mismatch_in_text(0)
        2
        """
    for i in range(self.patLen - 1, -1, -1):
        if currentPos + i >= self.textLen or self.pattern[i] != self.text[currentPos + i]:
            return i
    return -1