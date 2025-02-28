def render(pieces, style):
    """
    Render the given version pieces into the requested style.
    """
    if style == "full":
        return f"{pieces['major']}.{pieces['minor']}.{pieces['patch']}"
    elif style == "major":
        return f"{pieces['major']}"
    elif style == "minor":
        return f"{pieces['major']}.{pieces['minor']}"
    elif style == "patch":
        return f"{pieces['major']}.{pieces['minor']}.{pieces['patch']}"
    else:
        raise ValueError(f"Unknown style: {style}")