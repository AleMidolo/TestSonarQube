def render(pieces, style):
    """
    दिए गए संस्करण टुकड़ों को निर्दिष्ट शैली में प्रस्तुत करें।
    
    :param pieces: संस्करण टुकड़ों की सूची
    :param style: प्रस्तुति शैली
    :return: प्रस्तुत संस्करण
    """
    if style == "plain":
        return " ".join(pieces)
    elif style == "markdown":
        return "**" + " ".join(pieces) + "**"
    elif style == "html":
        return f"<p>{' '.join(pieces)}</p>"
    else:
        raise ValueError("असमर्थित शैली")