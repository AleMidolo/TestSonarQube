def validate_length_args(self, args):
    """
    दिए गए तर्कों की लंबाई की जाँच करें
    :param args: प्राप्त तर्क।  
    """
    if not args:
        raise ValueError("कोई तर्क प्रदान नहीं किया गया है।")
    if len(args) < 1:
        raise ValueError("तर्कों की संख्या अपर्याप्त है।")
    return True