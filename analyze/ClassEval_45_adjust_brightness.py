def adjust_brightness(self, factor):
    """
    Regola la luminosità dell'immagine se l'immagine è stata aperta.
    :param factor: float, luminosità di un'immagine. Un fattore di 0.0 produce un'immagine nera. Un fattore di 1.0 produce l'immagine originale.
    >>> processor.load_image('test.jpg')
    >>> processor.adjust_brightness(0.5)
    """
    from PIL import ImageEnhance
    
    if self.image is None:
        raise ValueError("Nessuna immagine caricata. Usa load_image() prima.")
    
    enhancer = ImageEnhance.Brightness(self.image)
    self.image = enhancer.enhance(factor)