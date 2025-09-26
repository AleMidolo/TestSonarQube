from PIL import Image, ImageEnhance, ImageChops


class ImageProcessor:
    def __init__(self):
        self.image = None

    def load_image(self, image_path):
        self.image = Image.open(image_path)

    def save_image(self, save_path):
        if self.image:
            self.image.save(save_path)

    def resize_image(self, width, height):
        self._resize((width, height))

    def rotate_image(self, degrees):
        self._rotate(degrees)

    def adjust_brightness(self, factor):
        self._adjust_brightness(factor)

    def _resize(self, size):
        if self.image:
            self.image = self.image.resize(size)

    def _rotate(self, degrees):
        if self.image:
            self.image = self.image.rotate(degrees)

    def _adjust_brightness(self, factor):
        if self.image:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)