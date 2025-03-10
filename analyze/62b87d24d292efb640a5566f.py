def render(pieces, style):
    """
    दिए गए संस्करण टुकड़ों को निर्दिष्ट शैली में प्रस्तुत करें।
    """
    if style == "plain":
        return " ".join(pieces)
    elif style == "bold":
        return "**" + " ".join(pieces) + "**"
    elif style == "italic":
        return "*" + " ".join(pieces) + "*"
    elif style == "code":
        return "`" + " ".join(pieces) + "`"
    else:
        return " ".join(pieces)  # Default to plain style if style is not recognized