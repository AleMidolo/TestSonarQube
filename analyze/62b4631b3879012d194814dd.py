def correggi_prefisso_namespace_w(contenuto):
    """
    Converte il testo che di default è 'w:st="' in 'w-st="'.
    """
    return contenuto.replace('w:st="', 'w-st="')