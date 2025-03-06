def test_tag(tag: str) -> bool:
    """
    Verifica se una parola può essere accettata come tag.
    
    Un tag è considerato valido se:
    - Non è vuoto.
    - Contiene solo caratteri alfanumerici o underscore (_).
    - Non inizia con un numero.
    
    :param tag: La stringa da verificare.
    :return: True se il tag è valido, False altrimenti.
    """
    if not tag:
        return False
    
    # Verifica che il tag contenga solo caratteri alfanumerici o underscore
    if not tag.replace("_", "").isalnum():
        return False
    
    # Verifica che il tag non inizi con un numero
    if tag[0].isdigit():
        return False
    
    return True