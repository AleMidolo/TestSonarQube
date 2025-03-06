def render(pieces, style):
    """
    दिए गए संस्करण टुकड़ों को निर्दिष्ट शैली में प्रस्तुत करें।
    
    :param pieces: संस्करण टुकड़ों की सूची
    :param style: प्रस्तुति शैली
    :return: शैली के अनुसार प्रस्तुत संस्करण
    """
    if style == "simple":
        return "\n".join(pieces)
    elif style == "detailed":
        return "\n".join([f"- {piece}" for piece in pieces])
    elif style == "json":
        import json
        return json.dumps(pieces, indent=4)
    else:
        raise ValueError("असमर्थित शैली")