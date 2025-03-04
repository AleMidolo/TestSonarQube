def validate_requires_args(self, args):
    """
    Verifica se sono stati forniti tutti gli argomenti richiesti.
    """
    if not args:
        return False
        
    for arg in self.required_args:
        if arg not in args:
            return False
            
    return True