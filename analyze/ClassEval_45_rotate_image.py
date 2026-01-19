def rotate_image(self, degrees):
    """
    如果图像已打开，则旋转图像
    :param degrees: float，图像将旋转的角度
    >>> processor.load_image('test.jpg')
    >>> processor.resize_image(90)
    """
    if hasattr(self, 'image') and self.image is not None:
        self.image = self.image.rotate(-degrees, expand=True)
    else:
        raise ValueError("No image loaded. Please load an image first.")