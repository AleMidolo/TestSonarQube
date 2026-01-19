def save_image(self, save_path):
    """
    Salva l'immagine in un percorso se l'immagine è stata aperta
    :param save_path: str, il percorso in cui l'immagine sarà salvata
    >>> processor.load_image('test.jpg')
    >>> processor.save_image('test2.jpg')
    """
    if self.image is not None:
        self.image.save(save_path)