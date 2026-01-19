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