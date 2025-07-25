def validate_length_args(self, args):
    """
    दिए गए तर्कों की लंबाई की जाँच करें
    :param args: प्राप्त तर्क।  
    """
    if not isinstance(args, (list, tuple)):
        raise TypeError("args must be a list or tuple")
    
    if len(args) == 0:
        raise ValueError("args must not be empty")
    
    return True