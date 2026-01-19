def rotate_image(self, degrees):
    """
        rota la imagen si la imagen está abierta
        :param degrees: float, los grados en los que se rotará la imagen
        >>> processor.load_image('test.jpg')
        >>> processor.rotate_image(90)
        """
    if self.image:
        self.image = self.image.rotate(degrees)