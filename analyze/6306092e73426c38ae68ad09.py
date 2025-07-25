def validate_length_args(self, args):
    """
    Verifica se il valore degli argomenti non supera la lunghezza specificata.  

    :param args: Gli argomenti ricevuti.  
    """
    for arg in args:
        if isinstance(arg, str):
            if len(arg) > self.max_length:
                raise ValueError(f"L'argomento '{arg}' supera la lunghezza massima consentita di {self.max_length} caratteri")
        elif isinstance(arg, (list, tuple, dict, set)):
            if len(arg) > self.max_length:
                raise ValueError(f"L'argomento di tipo {type(arg).__name__} supera la lunghezza massima consentita di {self.max_length} elementi")