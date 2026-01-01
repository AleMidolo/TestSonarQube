def interpret(self, display=False):
    """
        Interpreta la partitura musical que se va a tocar
        :param display: Bool, que representa si se debe imprimir la partitura interpretada
        :return: lista de dict, El dict incluye dos campos, Acorde y Melodía, que son letras y números, respectivamente. Si la entrada está vacía o contiene solo espacios en blanco, se devuelve una lista vacía.
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display = False)
        [{'Acorde': 'C', 'Melodía': '53231323'}, {'Acorde': 'Em', 'Melodía': '43231323'}, {'Acorde': 'F', 'Melodía': '43231323'}, {'Acorde': 'G', 'Melodía': '63231323'}]

        """
    if not self.play_text or self.play_text.isspace():
        return []
    result = []
    items = self.play_text.split()
    for item in items:
        chord = ''
        melody = ''
        i = 0
        while i < len(item) and (not item[i].isdigit()):
            chord += item[i]
            i += 1
        melody = item[i:]
        if chord and melody:
            result.append({'Acorde': chord, 'Melodía': melody})
            if display:
                print(self.display(chord, melody))
    return result