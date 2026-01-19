def load_image(self, image_path):
    """
    Utilizza l'utilità Image in PIL per aprire un'immagine
    :param image_path: str, percorso dell'immagine che deve essere
    >>> processor.load_image('test.jpg')
    >>> processor.image
    <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3072x4096 at 0x194F2412A48>
    """
    from PIL import Image
    self.image = Image.open(image_path)