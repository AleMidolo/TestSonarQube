def render(pieces, style):
    styled_pieces = []
    for piece in pieces:
        if style == "bold":
            styled_piece = f"**{piece}**"
        elif style == "italic":
            styled_piece = f"*{piece}*"
        elif style == "underline":
            styled_piece = f"__{piece}__"
        else:
            styled_piece = piece
        styled_pieces.append(styled_piece)
    return styled_pieces