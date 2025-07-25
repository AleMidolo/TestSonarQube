def register_vcs_handler(vcs, method):  # डेकोरेटर
    """
    एक डेकोरेटर बनाएं जो किसी विधि को VCS के हैंडलर के रूप में चिह्नित करे।

    def decorate(f):
        यह आंतरिक फ़ंक्शन डेकोरेटर के रूप में कार्य करता है।
    """
    def decorate(f):
        if not hasattr(f, '_vcs_handlers'):
            f._vcs_handlers = {}
        f._vcs_handlers[vcs] = method
        return f
    return decorate