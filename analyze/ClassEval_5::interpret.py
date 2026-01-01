def interpret(self, display=False):
    """
        Interpreta il punteggio musicale da suonare
        :param display: Bool, che rappresenta se stampare il punteggio interpretato
        :return: lista di dict, Il dict include due campi, Chord e Tune, che sono lettere e numeri, rispettivamente. Se l'input è vuoto o contiene solo spazi bianchi, viene restituita una lista vuota.
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display = False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]

        """
    if not self.play_text or self.play_text.isspace():
        return []
    result = []
    items = self.play_text.split()
    for item in items:
        chord = ''
        tune = ''
        i = 0
        while i < len(item) and (not item[i].isdigit()):
            chord += item[i]
            i += 1
        tune = item[i:]
        if chord and tune:
            result.append({'Chord': chord, 'Tune': tune})
            if display:
                print(self.display(chord, tune))
    return result