def validate_requires_args(self, args):
    """
    जांचें कि क्या सभी आवश्यक तर्क प्रदान किए गए हैं।
    """
    required_args = getattr(self, 'REQUIRED_ARGS', [])
    missing_args = [arg for arg in required_args if arg not in args]
    
    if missing_args:
        raise ValueError(f"Missing required arguments: {', '.join(missing_args)}")
    return True