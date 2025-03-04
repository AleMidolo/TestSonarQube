def validate_length_args(self, args):
    """
    दिए गए तर्कों की लंबाई की जाँच करें
    :param args: प्राप्त तर्क।  
    """
    if len(args) == 0:
        raise ValueError("No arguments provided")
    
    for arg in args:
        if not isinstance(arg, (str, list, tuple, dict)):
            continue
            
        if len(arg) == 0:
            raise ValueError(f"Empty argument provided: {arg}")