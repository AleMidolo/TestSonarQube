def interpret(self, display=False):
    """
    Interpret the music score to be played
    :param display:Bool, representing whether to print the interpreted score
    :return: list of dict, The dict includes two fields, Chord and Tune, which are letters and numbers, respectively. If the input is empty or contains only whitespace, an empty list is returned.
    >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
    >>> play_list = context.interpret(display = False)
    [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]

    """
    # Check if the input is empty or contains only whitespace
    if not hasattr(self, 'score') or not self.score or self.score.strip() == '':
        return []
    
    # Split the score by whitespace
    tokens = self.score.split()
    
    play_list = []
    
    for token in tokens:
        # Find where the chord (letters) ends and tune (numbers) begins
        chord = ''
        tune = ''
        
        for i, char in enumerate(token):
            if char.isdigit():
                # Found the start of the tune
                chord = token[:i]
                tune = token[i:]
                break
        
        # Only add if we found both chord and tune
        if chord and tune:
            play_list.append({'Chord': chord, 'Tune': tune})
    
    # Display if requested
    if display:
        print(play_list)
    
    return play_list