def adjust_brightness(self, factor):
    """
        Ajusta el brillo de la imagen si la imagen ha sido abierta.
        :param factor: float, brillo de una imagen. Un factor de 0.0 da una imagen negra. Un factor de 1.0 da la imagen original.
        >>> processor.load_image('test.jpg')
        >>> processor.adjust_brightness(0.5)
        """
    if self.image:
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(factor)