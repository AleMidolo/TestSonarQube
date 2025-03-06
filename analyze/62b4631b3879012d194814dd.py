def correggi_prefisso_namespace_w(contenuto):
    """
    Converte il testo che di default è 'w:st="' in 'w-st="'.
    
    Args:
        contenuto (str): Il testo da correggere.
    
    Returns:
        str: Il testo con il prefisso corretto.
    """
    return contenuto.replace('w:st="', 'w-st="')