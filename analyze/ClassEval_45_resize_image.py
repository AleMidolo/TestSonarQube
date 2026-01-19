def resize_image(self, width, height):
    """
    Redimensiona la imagen si la imagen está abierta.
    :param width: int, el ancho objetivo de la imagen
    :param height: int, la altura objetivo de la imagen
    >>> processor.load_image('test.jpg')
    >>> processor.resize_image(300, 300)
    >>> processor.image.width
    300
    >>> processor.image.height
    300
    """
    if self.image:
        self.image = self.image.resize((width, height))