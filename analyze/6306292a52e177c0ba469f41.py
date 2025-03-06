def test_tag(tag: str) -> bool:
    """
    Verifica se una parola può essere accettata come tag.
    
    Un tag è considerato valido se:
    - Non è vuoto.
    - Contiene solo caratteri alfanumerici e trattini bassi (_).
    - Non inizia o finisce con un trattino basso.
    - Non contiene spazi.
    
    :param tag: La stringa da verificare.
    :return: True se il tag è valido, False altrimenti.
    """
    if not tag:
        return False
    
    # Controlla che il tag non inizi o finisca con un trattino basso
    if tag.startswith('_') or tag.endswith('_'):
        return False
    
    # Controlla che il tag contenga solo caratteri alfanumerici e trattini bassi
    for char in tag:
        if not (char.isalnum() or char == '_'):
            return False
    
    return True