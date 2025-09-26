from PIL import Image, ImageEnhance, ImageChops


class ImageProcessor:
    def __init__(self):
        self._image = None

    def load_image(self, image_path):
        self._image = Image.open(image_path)

    def save_image(self, save_path):
        if self._image:
            self._image.save(save_path)

    def resize_image(self, width, height):
        self._resize(self._image, width, height)

    def rotate_image(self, degrees):
        self._rotate(self._image, degrees)

    def adjust_brightness(self, factor):
        self._adjust_brightness(self._image, factor)

    def _resize(self, image, width, height):
        if image:
            self._image = image.resize((width, height))

    def _rotate(self, image, degrees):
        if image:
            self._image = image.rotate(degrees)

    def _adjust_brightness(self, image, factor):
        if image:
            enhancer = ImageEnhance.Brightness(image)
            self._image = enhancer.enhance(factor)