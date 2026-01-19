def interpret(self, display=False):
    """
    Interpreta la partitura musical que se va a tocar
    :param display: Bool, que representa si se debe imprimir la partitura interpretada
    :return: lista de dict, El dict incluye dos campos, Acorde y Melodía, que son letras y números, respectivamente. Si la entrada está vacía o contiene solo espacios en blanco, se devuelve una lista vacía.
    >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
    >>> play_list = context.interpret(display = False)
    [{'Acorde': 'C', 'Melodía': '53231323'}, {'Acorde': 'Em', 'Melodía': '43231323'}, {'Acorde': 'F', 'Melodía': '43231323'}, {'Acorde': 'G', 'Melodía': '63231323'}]

    """
    # Verificar si la entrada está vacía o contiene solo espacios en blanco
    if not hasattr(self, 'score') or not self.score or self.score.strip() == '':
        return []
    
    # Dividir la partitura por espacios
    parts = self.score.strip().split()
    
    result = []
    
    for part in parts:
        if not part:  # Saltar partes vacías
            continue
        
        # Separar el acorde (letras) de la melodía (números)
        acorde = ''
        melodia = ''
        
        for char in part:
            if char.isalpha() or char == '#' or char == 'b':
                acorde += char
            elif char.isdigit():
                melodia += char
        
        # Solo agregar si hay tanto acorde como melodía
        if acorde and melodia:
            result.append({'Acorde': acorde, 'Melodía': melodia})
    
    # Mostrar si display es True
    if display:
        for item in result:
            print(f"Acorde: {item['Acorde']}, Melodía: {item['Melodía']}")
    
    return result