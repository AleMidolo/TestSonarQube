from PIL import Image, ImageEnhance, ImageChops

class ImageProcessor: 
    def __init__(self):
        """
        Initialize self.image
        """
        self.image = None

    def load_image(self, image_path):
        """
        Use Image util in PIL to open a image
        :param image_path: str, path of image that is to be
        >>> processor.load_image('test.jpg')
        >>> processor.image
        <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3072x4096 at 0x194F2412A48>
        """
        self.image = Image.open(image_path)

    def save_image(self, save_path):
        """
        Save image to a path if image has opened
        :param save_path: str, the path that the image will be saved
        >>> processor.load_image('test.jpg')
        >>> processor.save_image('test2.jpg')
        """
        if self.image:
            self.image.save(save_path)

    def rotate_image(self, degrees):
        """
        rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        >>> processor.load_image('test.jpg')
        >>> processor.rotate_image(90)
        """
        if self.image:
            self.image = self.image.rotate(degrees)

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        >>> processor.load_image('test.jpg')
        >>> processor.adjust_brightness(0.5)
        """
        if self.image:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)

    def resize_image(self, width, height):
        """
        यदि छवि खोली गई है तो छवि का आकार बदलें।
        :param width: int, छवि की लक्षित चौड़ाई
        :param height: int, छवि की लक्षित ऊँचाई
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(300, 300)
        >>> processor.image.width
        300
        >>> processor.image.height
        300
        """
        if self.image:
            self.image = self.image.resize((width, height))