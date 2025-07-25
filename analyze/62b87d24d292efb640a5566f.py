def render(pieces, style):
    """
    Renderizzare i pezzi forniti nella versione richiesta dello stile.
    """
    rendered = []
    
    # Dictionary mapping styles to piece representations
    styles = {
        'unicode': {
            'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
            'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
        },
        'ascii': {
            'K': 'K', 'Q': 'Q', 'R': 'R', 'B': 'B', 'N': 'N', 'P': 'P',
            'k': 'k', 'q': 'q', 'r': 'r', 'b': 'b', 'n': 'n', 'p': 'p'
        }
    }
    
    # Check if style exists
    if style not in styles:
        raise ValueError(f"Style '{style}' not supported")
        
    # Convert each piece to its styled representation
    for piece in pieces:
        if piece in styles[style]:
            rendered.append(styles[style][piece])
        else:
            rendered.append(piece)  # Keep unchanged if not a valid piece
            
    return rendered