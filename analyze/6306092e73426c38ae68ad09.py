def validate_length_args(self, args):
    """
    दिए गए तर्कों की लंबाई की जाँच करें
    :param args: प्राप्त तर्क।  
    """
    if len(args) == 0:
        raise ValueError("कोई तर्क नहीं दिया गया")
    
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError(f"अमान्य तर्क प्रकार: {type(arg)}। संख्यात्मक तर्क आवश्यक हैं।")
            
        if arg <= 0:
            raise ValueError(f"अमान्य तर्क मान: {arg}। धनात्मक संख्या आवश्यक है।")