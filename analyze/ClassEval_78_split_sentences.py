def split_sentences(self, sentences_string):
    """
    Divide una cadena en una lista de oraciones. Las oraciones terminan con . o ? y con un espacio después de eso. Tenga en cuenta que Sr. también termina con . pero no son oraciones.
    :param sentences_string: string, cadena a dividir
    :return:list, lista de oraciones divididas
    >>> ss = SplitSentence()
    >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
    ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
    """
    import re
    
    # Patrón que busca . o ? seguidos de un espacio (pero no Sr.)
    # Usamos lookahead negativo para evitar dividir en "Sr."
    pattern = r'(?<!Sr)([.?])\s+'
    
    # Dividir por el patrón pero mantener el delimitador
    parts = re.split(pattern, sentences_string)
    
    # Reconstruir las oraciones combinando el texto con su puntuación
    sentences = []
    i = 0
    while i < len(parts):
        if i + 1 < len(parts) and parts[i + 1] in '.?':
            # Combinar texto con su puntuación
            sentences.append(parts[i] + parts[i + 1])
            i += 2
        elif parts[i].strip():  # Si hay texto restante
            sentences.append(parts[i])
            i += 1
        else:
            i += 1
    
    return sentences