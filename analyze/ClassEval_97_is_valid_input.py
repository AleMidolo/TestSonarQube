def is_valid_input(self, textnum):
    """
        जांचें कि इनपुट पाठ में केवल मान्य शब्द हैं जिन्हें संख्याओं में परिवर्तित किया जा सकता है।
        :param textnum: इनपुट पाठ जिसमें संख्याओं का प्रतिनिधित्व करने वाले शब्द हैं।
        :return: यदि इनपुट मान्य है तो True, अन्यथा False।
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
    valid_words = set(self.numwords.keys()).union(set(self.ordinal_words.keys()))
    words = textnum.replace('-', ' ').split()
    return all((word in valid_words for word in words))