def save_image(self, save_path):
    """
    Guarda la imagen en una ruta si la imagen ha sido abierta
    :param save_path: str, la ruta en la que se guardará la imagen
    >>> processor.load_image('test.jpg')
    >>> processor.save_image('test2.jpg')
    """
    if self.image is not None:
        self.image.save(save_path)
    else:
        raise ValueError("No image has been loaded. Please load an image first using load_image().")