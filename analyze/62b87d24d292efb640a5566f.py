def render(pieces, style):
    """
    दिए गए संस्करण टुकड़ों को निर्दिष्ट शैली में प्रस्तुत करें।
    """
    styled_pieces = []
    for piece in pieces:
        styled_piece = f"{style}: {piece}"
        styled_pieces.append(styled_piece)
    return "\n".join(styled_pieces)