def save_image(self, save_path):
    """
    如果图像已打开，则将图像保存到指定路径
    :param save_path: str，图像将被保存的路径
    >>> processor.load_image('test.jpg')
    >>> processor.save_image('test2.jpg')
    """
    if hasattr(self, 'image') and self.image is not None:
        self.image.save(save_path)
    else:
        raise ValueError("No image loaded. Please load an image first using load_image().")