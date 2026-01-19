def interpret(self, display=False):
    """
        Interpret the music score to be played
        :param display:Bool, representing whether to print the interpreted score
        :return: list of dict, The dict includes two fields, Chord and Tune, which are letters and numbers, respectively. If the input is empty or contains only whitespace, an empty list is returned.
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