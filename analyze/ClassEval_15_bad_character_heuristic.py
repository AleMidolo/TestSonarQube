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
    result = []
    
    # Preprocessing: create bad character table
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i
    
    # Searching
    s = 0  # shift of the pattern with respect to text
    while s <= n - m:
        j = m - 1
        
        # Keep reducing j while characters of pattern and text match
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        # If pattern is present at current shift
        if j < 0:
            result.append(s)
            # Shift pattern so that next character in text aligns with last occurrence in pattern
            s += (m - bad_char.get(text[s + m], -1) - 1) if s + m < n else 1
        else:
            # Shift pattern so that bad character in text aligns with last occurrence in pattern
            s += max(1, j - bad_char.get(text[s + j], -1))
    
    return result