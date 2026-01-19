def load_image(self, image_path):
    """
    Utiliza la utilidad Image en PIL para abrir una imagen
    :param image_path: str, ruta de la imagen que se va a
    >>> processor.load_image('test.jpg')
    >>> processor.image
    <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3072x4096 at 0x194F2412A48>
    """
    from PIL import Image
    self.image = Image.open(image_path)