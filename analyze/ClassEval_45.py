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
        self._resize_image((width, height))

    def rotate_image(self, degrees):
        self._rotate_image(degrees)

    def adjust_brightness(self, factor):
        self._adjust_brightness(factor)

    def _resize_image(self, size):
        if self._image:
            self._image = self._image.resize(size)

    def _rotate_image(self, degrees):
        if self._image:
            self._image = self._image.rotate(degrees)

    def _adjust_brightness(self, factor):
        if self._image:
            enhancer = ImageEnhance.Brightness(self._image)
            self._image = enhancer.enhance(factor)