class AutomaticGuitarSimulator: 
    def __init__(self, text) -> None:
        """
        Initialize the score to be played
        :param text:str, score to be played
        """
        self.play_text = text

    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return: str
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.display("C", "53231323")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323
        """
        return "Normal Guitar Playing -- Chord: %s, Play Tune: %s" % (key, value)

    def interpret(self, display=False):
        """
        Interpreta il punteggio musicale da suonare
        :param display: Bool, che rappresenta se stampare il punteggio interpretato
        :return: lista di dict, Il dict include due campi, Chord e Tune, che sono lettere e numeri, rispettivamente. Se l'input è vuoto o contiene solo spazi bianchi, viene restituita una lista vuota.
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display = False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]
        """
        if not self.play_text.strip():
            return []
        
        chords_and_tunes = []
        import re
        matches = re.findall(r'([A-G][#b]?m?)(\d+)', self.play_text)
        
        for chord, tune in matches:
            chords_and_tunes.append({'Chord': chord, 'Tune': tune})
            if display:
                print(self.display(chord, tune))
        
        return chords_and_tunes