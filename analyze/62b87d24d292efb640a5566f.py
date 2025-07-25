def render(pieces, style):
    """
    दिए गए संस्करण टुकड़ों को निर्दिष्ट शैली में प्रस्तुत करें।
    
    :param pieces: संस्करण टुकड़ों की सूची
    :param style: प्रस्तुति शैली
    :return: शैली के अनुसार प्रस्तुत संस्करण
    """
    if style == "plain":
        return " ".join(pieces)
    elif style == "markdown":
        return f"**{' '.join(pieces)}**"
    elif style == "html":
        return f"<h1>{' '.join(pieces)}</h1>"
    else:
        raise ValueError("असमर्थित शैली")