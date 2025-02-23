def validate_requires_args(self, args):
    """
    Verifica se sono stati forniti tutti gli argomenti richiesti.
    """
    required_args = self.get_required_args()  # Supponendo che ci sia un metodo per ottenere gli argomenti richiesti
    missing_args = [arg for arg in required_args if arg not in args]
    
    if missing_args:
        raise ValueError(f"Missing required arguments: {', '.join(missing_args)}")
    
    return True