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
    if not hasattr(self, 'score') or not self.score or self.score.strip() == '':
        return []
    
    # Split the score by spaces
    parts = self.score.strip().split()
    
    result = []
    
    for part in parts:
        if not part:  # Skip empty strings
            continue
        
        # Find where the chord ends and the melody begins
        # The chord is the initial letters, the melody is the numbers
        chord = ''
        melody = ''
        
        for i, char in enumerate(part):
            if char.isdigit():
                chord = part[:i]
                melody = part[i:]
                break
        
        # Only add if we found both chord and melody
        if chord and melody:
            result.append({'Acorde': chord, 'Melodía': melody})
    
    # Display if requested
    if display:
        for item in result:
            print(f"Acorde: {item['Acorde']}, Melodía: {item['Melodía']}")
    
    return result