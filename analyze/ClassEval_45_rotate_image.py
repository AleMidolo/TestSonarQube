def rotate_image(self, degrees):
    """
    ruota l'immagine se l'immagine è stata aperta
    :param degrees: float, i gradi con cui l'immagine verrà ruotata
    >>> processor.load_image('test.jpg')
    >>> processor.resize_image(90)
    """
    if self.image is not None:
        self.image = self.image.rotate(degrees, expand=True)
    else:
        raise ValueError("No image loaded. Please load an image first.")