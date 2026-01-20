def rotate_image(self, degrees):
    """
    rota la imagen si la imagen está abierta
    :param degrees: float, los grados en los que se rotará la imagen
    >>> processor.load_image('test.jpg')
    >>> processor.resize_image(90)
    """
    if hasattr(self, 'image') and self.image is not None:
        self.image = self.image.rotate(degrees, expand=True)
    else:
        raise ValueError("No image is currently loaded. Please load an image first.")