def render(pieces, style):
    """
    दिए गए संस्करण टुकड़ों को निर्दिष्ट शैली में प्रस्तुत करें।
    """
    if not pieces:
        return ""
        
    if style == "plain":
        return "".join(pieces)
    elif style == "html":
        return "<div>" + "".join(pieces) + "</div>"
    elif style == "markdown":
        return "**" + "".join(pieces) + "**"
    else:
        return "".join(pieces)