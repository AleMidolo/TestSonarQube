def validate_requires_args(self, args):
    """
    Verifica se sono stati forniti tutti gli argomenti richiesti.
    """
    if not args:
        raise ValueError("Nessun argomento fornito.")
    return True