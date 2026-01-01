def is_valid_input(self, textnum):
    """
        जांचें कि इनपुट पाठ में केवल मान्य शब्द हैं जिन्हें संख्याओं में परिवर्तित किया जा सकता है।
        :param textnum: इनपुट पाठ जिसमें संख्याओं का प्रतिनिधित्व करने वाले शब्द हैं।
        :return: यदि इनपुट मान्य है तो True, अन्यथा False।
        >>> w2n = Words2Numbers()
        >>> w2n.is_valid_input("thirty-two")
        False
        """
    textnum = textnum.replace('-', ' ')
    words = textnum.split()
    for word in words:
        if word in self.ordinal_words:
            continue
        is_ordinal = False
        for ending, replacement in self.ordinal_endings:
            if word.endswith(ending):
                base_word = word[:-len(ending)] + replacement
                if base_word in self.numwords:
                    is_ordinal = True
                    break
        if is_ordinal:
            continue
        if word not in self.numwords:
            return False
    return True