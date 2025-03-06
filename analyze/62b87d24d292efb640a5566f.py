def render(pieces, style):
    """
    दिए गए संस्करण टुकड़ों को निर्दिष्ट शैली में प्रस्तुत करें।
    """
    if style == "simple":
        return ".".join(map(str, pieces))
    elif style == "full":
        return f"v{'.'.join(map(str, pieces))}"
    elif style == "tag":
        return f"v{'.'.join(map(str, pieces))}"
    else:
        raise ValueError("अमान्य शैली। समर्थित शैलियाँ हैं: 'simple', 'full', 'tag'")