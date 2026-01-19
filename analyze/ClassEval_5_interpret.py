def interpret(self, display=False):
    """
    Interpreta il punteggio musicale da suonare
    :param display: Bool, che rappresenta se stampare il punteggio interpretato
    :return: lista di dict, Il dict include due campi, Chord e Tune, che sono lettere e numeri, rispettivamente. Se l'input è vuoto o contiene solo spazi bianchi, viene restituita una lista vuota.
    >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
    >>> play_list = context.interpret(display = False)
    [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]

    """
    # Check if input is empty or contains only whitespace
    if not hasattr(self, 'score') or not self.score or self.score.strip() == '':
        return []
    
    # Split the score by spaces
    tokens = self.score.strip().split()
    
    play_list = []
    
    for token in tokens:
        if not token:  # Skip empty tokens
            continue
        
        # Separate chord (letters) from tune (numbers)
        chord = ''
        tune = ''
        
        for char in token:
            if char.isalpha():
                chord += char
            elif char.isdigit():
                tune += char
        
        # Only add if we have both chord and tune
        if chord and tune:
            play_list.append({'Chord': chord, 'Tune': tune})
    
    # Display if requested
    if display:
        print(play_list)
    
    return play_list