def rotate_image(self, degrees):
    """
        rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        >>> processor.load_image('test.jpg')
        >>> processor.rotate_image(90)
        >>> processor.image.size
        (4096, 3072)
        """
    if self.image:
        self.image = self.image.rotate(degrees)