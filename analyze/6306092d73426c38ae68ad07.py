def validate_requires_args(self, args):
    """
    जांचें कि क्या सभी आवश्यक तर्क प्रदान किए गए हैं।
    """
    if not args:
        raise ValueError("Required arguments are missing")
        
    for arg in args:
        if arg is None:
            raise ValueError(f"Required argument {arg} is missing")
            
    return True