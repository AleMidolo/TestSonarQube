def match_in_pattern(self, char):
    """
    पैटर्न में किसी वर्ण की सबसे दाईं उपस्थिति को खोजता है।
    :param char: खोजा जाने वाला वर्ण, str.
    :return: पैटर्न में वर्ण की सबसे दाईं उपस्थिति का अनुक्रमांक, int.
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
    >>> boyerMooreSearch.match_in_pattern("A")
    0

    """
    # Search for the rightmost occurrence of char in the pattern
    # Iterate from right to left through the pattern
    for i in range(len(self.pattern) - 1, -1, -1):
        if self.pattern[i] == char:
            return i
    # If character not found, return -1
    return -1