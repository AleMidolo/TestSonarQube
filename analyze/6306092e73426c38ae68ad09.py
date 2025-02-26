def validate_length_args(self, args):
    """
    दिए गए तर्कों की लंबाई की जाँच करें
    :param args: प्राप्त तर्क।  
    """
    if not isinstance(args, (list, tuple)):
        raise ValueError("args must be a list or tuple")
    
    length = len(args)
    if length == 0:
        raise ValueError("args cannot be empty")
    
    return length