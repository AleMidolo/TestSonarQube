def adjust_brightness(self, factor):
    """
    Adjust the brightness of image if image has opened.
    :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
    >>> processor.load_image('test.jpg')
    >>> processor.adjust_brightness(0.5)
    """
    if self.image is None:
        raise ValueError("No image loaded. Please load an image first.")
    
    from PIL import ImageEnhance
    
    enhancer = ImageEnhance.Brightness(self.image)
    self.image = enhancer.enhance(factor)