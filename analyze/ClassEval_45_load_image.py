def load_image(self, image_path):
    """
    使用PIL中的Image工具打开图像
    :param image_path: str，待处理图像的路径
    >>> processor.load_image('test.jpg')
    >>> processor.image
    <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3072x4096 at 0x194F2412A48>
    """
    from PIL import Image
    self.image = Image.open(image_path)