def validate_requires_args(self, args):
    """
    Check if all the required arguments have been provided.
    """
    if not hasattr(self, 'required_args'):
        return True
        
    for required_arg in self.required_args:
        if required_arg not in args:
            return False
            
    return True