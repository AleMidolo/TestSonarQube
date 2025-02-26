def render(pieces, style):
    """
    Render the given version pieces into the requested style.
    """
    if style == 'html':
        return ''.join(f'<div>{piece}</div>' for piece in pieces)
    elif style == 'markdown':
        return '\n'.join(f'* {piece}' for piece in pieces)
    elif style == 'plain':
        return '\n'.join(pieces)
    else:
        raise ValueError("Unsupported style. Choose 'html', 'markdown', or 'plain'.")