def render(pieces, style):
    """
    दिए गए संस्करण टुकड़ों को निर्दिष्ट शैली में प्रस्तुत करें।
    
    :param pieces: संस्करण टुकड़ों की सूची
    :param style: प्रस्तुति शैली
    :return: प्रस्तुत संस्करण
    """
    if style == "default":
        return ".".join(map(str, pieces))
    elif style == "verbose":
        return f"संस्करण: {'.'.join(map(str, pieces))}"
    elif style == "json":
        import json
        return json.dumps({"version": pieces})
    else:
        raise ValueError("अमान्य शैली")