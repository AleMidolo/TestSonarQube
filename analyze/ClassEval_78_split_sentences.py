def split_sentences(self, sentences_string):
    """
    Suddivide una stringa in una lista di frasi. Le frasi terminano con . o ? e con uno spazio dopo. Si prega di notare che Mr. termina anch'esso con . ma non è una frase.
    :param sentences_string: stringa, stringa da suddividere
    :return: lista, lista delle frasi suddivise
    >>> ss = SplitSentence()
    >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
    ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
    """
    import re
    
    # Pattern che identifica . o ? seguiti da uno spazio, ma non Mr.
    # Usa lookahead negativo per escludere Mr.
    pattern = r'(?<!Mr)([.?])\s+'
    
    # Dividi la stringa usando il pattern
    parts = re.split(pattern, sentences_string)
    
    # Ricostruisci le frasi combinando il testo con i delimitatori
    sentences = []
    i = 0
    while i < len(parts):
        if i + 1 < len(parts) and parts[i + 1] in '.?':
            # Combina il testo con il suo delimitatore
            sentences.append(parts[i] + parts[i + 1])
            i += 2
        else:
            # Ultimo elemento senza delimitatore o testo rimanente
            if parts[i].strip():
                sentences.append(parts[i].strip())
            i += 1
    
    return sentences