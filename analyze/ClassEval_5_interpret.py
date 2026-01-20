def interpret(self, display=False):
    """
    Interpreta la partitura musical que se va a tocar
    :param display: Bool, que representa si se debe imprimir la partitura interpretada
    :return: lista de dict, El dict incluye dos campos, Acorde y Melodía, que son letras y números, respectivamente. Si la entrada está vacía o contiene solo espacios en blanco, se devuelve una lista vacía.
    >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
    >>> play_list = context.interpret(display = False)
    [{'Acorde': 'C', 'Melodía': '53231323'}, {'Acorde': 'Em', 'Melodía': '43231323'}, {'Acorde': 'F', 'Melodía': '43231323'}, {'Acorde': 'G', 'Melodía': '63231323'}]

    """
    # Check if the input is empty or contains only whitespace
    if not hasattr(self, 'partitura') or not self.partitura or self.partitura.strip() == '':
        return []
    
    # Split the partitura by spaces
    tokens = self.partitura.strip().split()
    
    result = []
    
    for token in tokens:
        if not token:  # Skip empty tokens
            continue
        
        # Find where the chord ends and the melody begins
        # The chord is the initial letters, the melody is the numbers
        i = 0
        while i < len(token) and not token[i].isdigit():
            i += 1
        
        acorde = token[:i]
        melodia = token[i:]
        
        # Only add if we have both chord and melody
        if acorde and melodia:
            result.append({'Acorde': acorde, 'Melodía': melodia})
    
    # Display if requested
    if display:
        print(result)
    
    return result