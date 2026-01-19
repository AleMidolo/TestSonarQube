def rotate_image(self, degrees):
    """
    rotate image if image has opened
    :param degrees: float, the degrees that the image will be rotated
    >>> processor.load_image('test.jpg')
    >>> processor.resize_image(90)
    """
    if hasattr(self, 'image') and self.image is not None:
        self.image = self.image.rotate(degrees, expand=True)
    else:
        raise ValueError("No image loaded. Please load an image first.")