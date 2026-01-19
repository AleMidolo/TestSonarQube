def bad_character_heuristic(self):
    """
    Trova tutte le occorrenze del pattern nel testo.
    :return: Una lista di tutte le posizioni del modello nel testo, lista.
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
    
    # Preprocessing: create bad character table
    bad_char = {}
    for i in range(m - 1):
        bad_char[pattern[i]] = m - 1 - i
    
    # Search phase
    results = []
    s = 0  # shift of the pattern with respect to text
    
    while s <= n - m:
        j = m - 1
        
        # Keep reducing j while characters match
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        # If pattern is found at current shift
        if j < 0:
            results.append(s)
            s += 1
        else:
            # Shift pattern using bad character heuristic
            bad_char_shift = bad_char.get(text[s + j], m)
            s += max(1, bad_char_shift - (m - 1 - j))
    
    return results