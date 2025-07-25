def fix_namespace_prefix_w(content):
    """
    Convierte el texto que por defecto es 'w:st="' a 'w-st="'
    """
    return content.replace('w:st="', 'w-st="')