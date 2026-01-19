def mismatch_in_text(self, currentPos):
    """
    पैटर्न और टेक्स्ट के बीच पहले असमानता की स्थिति निर्धारित करता है।
    :param currentPos: टेक्स्ट में वर्तमान स्थिति, int.
    :return: पैटर्न और टेक्स्ट के बीच पहले असमानता की स्थिति, int, अन्यथा -1।
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
    >>> boyerMooreSearch.mismatch_in_text(0)
    2

    """
    # Compare pattern with text from right to left
    for i in range(len(self.pattern) - 1, -1, -1):
        # Check if we're within text bounds
        if currentPos + i >= len(self.text):
            return i
        # Check for mismatch
        if self.pattern[i] != self.text[currentPos + i]:
            return i
    # No mismatch found, pattern matches completely
    return -1