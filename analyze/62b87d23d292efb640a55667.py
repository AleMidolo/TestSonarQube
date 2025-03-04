def register_vcs_handler(vcs, method):  # डेकोरेटर
    """
    एक डेकोरेटर बनाएं जो किसी विधि को VCS के हैंडलर के रूप में चिह्नित करे।
    """
    def decorate(f):
        # हैंडलर रजिस्टर करने के लिए एक डिक्शनरी बनाएं अगर नहीं है
        if not hasattr(f, '_vcs_handlers'):
            f._vcs_handlers = {}
        
        # विधि को हैंडलर के रूप में रजिस्टर करें
        if vcs not in f._vcs_handlers:
            f._vcs_handlers[vcs] = []
        f._vcs_handlers[vcs].append(method)
        
        return f
        
    return decorate