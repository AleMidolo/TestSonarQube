def validate_requires_args(self, args):
    """
    检查是否提供了所有必需的参数。
    """
    if not args:
        raise ValueError("No arguments provided")
        
    required_args = getattr(self, 'required_args', [])
    
    for arg in required_args:
        if arg not in args:
            raise ValueError(f"Missing required argument: {arg}")
            
    return True