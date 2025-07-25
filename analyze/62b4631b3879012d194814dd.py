def fix_namespace_prefix_w(content):
    """
    Convert text that defaults to 'w:st="' to 'w-st="'
    """
    return content.replace('w:st="', 'w-st="')