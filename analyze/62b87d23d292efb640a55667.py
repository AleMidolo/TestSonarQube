def register_vcs_handler(vcs, method):  # डेकोरेटर
    """
    एक डेकोरेटर बनाएं जो किसी विधि को VCS के हैंडलर के रूप में चिह्नित करे।

    def decorate(f):
        यह आंतरिक फ़ंक्शन डेकोरेटर के रूप में कार्य करता है।    
    """
    def decorate(f):
        # यहाँ पर VCS हैंडलर को चिह्नित करने की लॉजिक डालें
        f.vcs_handler = True
        f.vcs_type = vcs
        f.method = method
        return f
    return decorate