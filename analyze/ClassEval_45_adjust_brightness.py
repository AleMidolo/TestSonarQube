def adjust_brightness(self, factor):
    """
    यदि छवि खोली गई है तो छवि की चमक को समायोजित करें।
    :param factor: float, एक छवि की चमक। 0.0 का एक कारक एक काली छवि देता है। 1.0 का एक कारक मूल छवि देता है।
    >>> processor.load_image('test.jpg')
    >>> processor.adjust_brightness(0.5)
    """
    if self.image is None:
        raise ValueError("No image loaded. Please load an image first.")
    
    from PIL import ImageEnhance
    
    enhancer = ImageEnhance.Brightness(self.image)
    self.image = enhancer.enhance(factor)