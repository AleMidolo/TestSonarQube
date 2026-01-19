def mismatch_in_text(self, currentPos):
    """
    पैटर्न और टेक्स्ट के बीच पहले असमानता की स्थिति निर्धारित करता है।
    :param currentPos: टेक्स्ट में वर्तमान स्थिति, int.
    :return: पैटर्न और टेक्स्ट के बीच पहले असमानता की स्थिति, int, अन्यथा -1।
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
    >>> boyerMooreSearch.mismatch_in_text(0)
    2

    """
    # पैटर्न के अंत से शुरू करके तुलना करें
    for i in range(len(self.pattern) - 1, -1, -1):
        # जांचें कि टेक्स्ट में पर्याप्त वर्ण हैं
        if currentPos + i >= len(self.text):
            return i
        # यदि वर्ण मेल नहीं खाते हैं, तो पैटर्न में असमानता की स्थिति लौटाएं
        if self.pattern[i] != self.text[currentPos + i]:
            return i
    # यदि सभी वर्ण मेल खाते हैं, तो -1 लौटाएं
    return -1