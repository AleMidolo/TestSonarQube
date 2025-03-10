def test_tag(tag: str) -> bool:
    """
    Verifica se una parola può essere accettata come tag.
    
    Un tag è considerato valido se:
    - Non è vuoto.
    - Contiene solo caratteri alfanumerici e trattini bassi (_).
    - Non inizia con un numero.
    - Ha una lunghezza massima di 50 caratteri.
    
    :param tag: La stringa da verificare.
    :return: True se il tag è valido, False altrimenti.
    """
    if not tag:
        return False
    
    if len(tag) > 50:
        return False
    
    if tag[0].isdigit():
        return False
    
    for char in tag:
        if not (char.isalnum() or char == '_'):
            return False
    
    return True