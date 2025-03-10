def unquote(name):
    """
    दिए गए नाम से उद्धरण (quotes) को हटाने के लिए फ़ंक्शन।
    """
    if name.startswith('"') and name.endswith('"'):
        return name[1:-1]
    elif name.startswith("'") and name.endswith("'"):
        return name[1:-1]
    return name