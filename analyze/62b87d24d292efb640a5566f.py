def render(pieces, style):
    """
    Renderizzare i pezzi forniti nella versione richiesta dello stile.
    """
    rendered = []
    
    # Dictionary mapping piece names to unicode chess symbols
    unicode_pieces = {
        'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
        'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
    }
    
    # Dictionary mapping piece names to ASCII representations
    ascii_pieces = {
        'K': 'K', 'Q': 'Q', 'R': 'R', 'B': 'B', 'N': 'N', 'P': 'P',
        'k': 'k', 'q': 'q', 'r': 'r', 'b': 'b', 'n': 'n', 'p': 'p'
    }
    
    # Select style mapping
    piece_map = unicode_pieces if style == 'unicode' else ascii_pieces
    
    # Render each piece according to selected style
    for piece in pieces:
        if piece in piece_map:
            rendered.append(piece_map[piece])
        else:
            rendered.append(piece)  # Keep non-piece characters as-is
            
    return ''.join(rendered)