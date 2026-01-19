def adjust_brightness(self, factor):
    """
    如果图像已打开，调整图像的亮度。
    :param factor: float，图像的亮度。因子为0.0时生成黑色图像。因子为1.0时生成原始图像。
    >>> processor.load_image('test.jpg')
    >>> processor.adjust_brightness(0.5)
    """
    from PIL import ImageEnhance
    
    if self.image is not None:
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(factor)