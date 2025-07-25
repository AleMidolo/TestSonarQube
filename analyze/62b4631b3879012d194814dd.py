def fix_namespace_prefix_w(content):
    """
    Converte il testo che di default è 'w:st="' in 'w-st="'.
    """
    return content.replace('w:st="', 'w-st="')