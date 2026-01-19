def resize_image(self, width, height):
    """
    Risize the image if image has opened.
    :param width: int, the target width of image
    :param height: int, the target height of image
    >>> processor.load_image('test.jpg')
    >>> processor.resize_image(300, 300)
    >>> processor.image.width
    300
    >>> processor.image.height
    300
    """
    if self.image is not None:
        self.image = self.image.resize((width, height))