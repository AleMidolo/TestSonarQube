def validate_requires_args(self, args):
    """
    检查是否提供了所有必需的参数。
    """
    required_args = self.required_args  # Assuming required_args is a list of required argument names
    missing_args = [arg for arg in required_args if arg not in args]
    
    if missing_args:
        raise ValueError(f"Missing required arguments: {', '.join(missing_args)}")
    return True