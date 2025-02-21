def validate_choices_args(self, args):  
    """
    Verifica se il valore degli argomenti di scelta è una delle opzioni disponibili.  

    :param args: Gli argomenti ricevuti.  
    """
    available_choices = self.get_available_choices()  # Supponendo che ci sia un metodo per ottenere le scelte disponibili
    for arg in args:
        if arg not in available_choices:
            raise ValueError(f"'{arg}' non è una scelta valida. Scelte disponibili: {available_choices}")