def bad_character_heuristic(self):
    """
    Finds all occurrences of the pattern in the text.
    :return: A list of all positions of the pattern in the text, list.
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
    >>> boyerMooreSearch.bad_character_heuristic()
    [0, 3]

    """
    text = self.text
    pattern = self.pattern
    m = len(pattern)
    n = len(text)
    
    if m == 0 or n == 0 or m > n:
        return []
    
    # Build bad character table
    bad_char = {}
    for i in range(m - 1):
        bad_char[pattern[i]] = m - 1 - i
    
    # Search for pattern
    results = []
    s = 0  # shift of the pattern with respect to text
    
    while s <= n - m:
        j = m - 1
        
        # Keep reducing j while characters match
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        # If pattern is found
        if j < 0:
            results.append(s)
            # Shift pattern to align with next possible match
            s += 1
        else:
            # Shift pattern based on bad character heuristic
            bad_char_shift = bad_char.get(text[s + j], m)
            s += max(1, bad_char_shift - (m - 1 - j))
    
    return results