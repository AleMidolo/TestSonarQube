def unquote(name):
    """
    दिए गए नाम से उद्धरण (quotes) को हटाने के लिए फ़ंक्शन।
    """
    # Remove single and double quotes from start and end if present
    if name:
        if (name[0] == '"' and name[-1] == '"') or (name[0] == "'" and name[-1] == "'"):
            return name[1:-1]
    return name