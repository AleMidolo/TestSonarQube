def bad_character_heuristic(self):
    """
    Encuentra todas las ocurrencias del patrón en el texto.
    :return: Una lista de todas las posiciones del patrón en el texto, lista.
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
    >>> boyerMooreSearch.bad_character_heuristic()
    [0, 3]

    """
    text = self.text
    pattern = self.pattern
    m = len(pattern)
    n = len(text)
    result = []
    
    # Crear tabla de caracteres malos
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i
    
    s = 0  # desplazamiento del patrón respecto al texto
    
    while s <= n - m:
        j = m - 1
        
        # Reducir j mientras los caracteres coincidan
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        # Si el patrón está presente en la posición actual
        if j < 0:
            result.append(s)
            # Desplazar el patrón para alinear el siguiente carácter en el texto
            s += (m - bad_char.get(text[s + m], -1) - 1) if s + m < n else 1
        else:
            # Desplazar el patrón basándose en la heurística del carácter malo
            s += max(1, j - bad_char.get(text[s + j], -1))
    
    return result