def validate_length_args(self, args):  
    """
    Verifica se il valore degli argomenti non supera la lunghezza specificata.  

    :param args: Gli argomenti ricevuti.  
    """
    max_length = 100  # Imposta la lunghezza massima consentita
    for arg in args:
        if len(arg) > max_length:
            raise ValueError(f"L'argomento '{arg}' supera la lunghezza massima di {max_length}.")
    return True