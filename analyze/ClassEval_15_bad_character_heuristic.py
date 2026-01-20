def bad_character_heuristic(self):
    """
    Encuentra todas las ocurrencias del patrón en el texto.
    :return: Una lista de todas las posiciones del patrón en el texto, lista.
    >>> boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
    >>> boyerMooreSearch.bad_character_heuristic()
    [0, 3]

    """
    result = []
    text = self.text
    pattern = self.pattern
    m = len(pattern)
    n = len(text)
    
    if m == 0 or n == 0 or m > n:
        return result
    
    # Crear tabla de caracteres malos
    bad_char = {}
    for i in range(m - 1):
        bad_char[pattern[i]] = m - 1 - i
    
    # Búsqueda
    s = 0  # desplazamiento del patrón respecto al texto
    while s <= n - m:
        j = m - 1
        
        # Reducir j mientras los caracteres coincidan
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        # Si el patrón está presente en el desplazamiento actual
        if j < 0:
            result.append(s)
            # Mover el patrón para alinearlo con el siguiente carácter
            s += 1
        else:
            # Desplazar el patrón usando la heurística del carácter malo
            bad_char_shift = bad_char.get(text[s + j], m)
            s += max(1, bad_char_shift - (m - 1 - j))
    
    return result