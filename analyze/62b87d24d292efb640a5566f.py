def render(pieces, style):
    """
    Renderizzare i pezzi forniti nella versione richiesta dello stile.
    """
    rendered = []
    
    for piece in pieces:
        if style == "unicode":
            # Unicode chess piece symbols
            symbols = {
                "K": "♔", "Q": "♕", "R": "♖", "B": "♗", "N": "♘", "P": "♙",
                "k": "♚", "q": "♛", "r": "♜", "b": "♝", "n": "♞", "p": "♟"
            }
            rendered.append(symbols.get(piece, piece))
            
        elif style == "ascii":
            # ASCII representations
            symbols = {
                "K": "K", "Q": "Q", "R": "R", "B": "B", "N": "N", "P": "P",
                "k": "k", "q": "q", "r": "r", "b": "b", "n": "n", "p": "p"
            }
            rendered.append(symbols.get(piece, piece))
            
        elif style == "algebraic":
            # Algebraic notation
            symbols = {
                "K": "K", "Q": "Q", "R": "R", "B": "B", "N": "N", "P": "",
                "k": "K", "q": "Q", "r": "R", "b": "B", "n": "N", "p": ""
            }
            rendered.append(symbols.get(piece, piece))
            
        else:
            # Default to returning the piece unchanged
            rendered.append(piece)
            
    return "".join(rendered)