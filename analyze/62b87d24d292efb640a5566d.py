def plus_or_dot(pieces):
    # Check if any piece has a "+" in its closet-tag
    has_plus = any("+" in piece.get("closet-tag", "") for piece in pieces)
    
    # Return "." if "+" exists, otherwise return "+"
    return "." if has_plus else "+"