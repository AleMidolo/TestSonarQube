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
        self._check_image_loaded()
        self.image = self.image.resize((width, height))

    def rotate_image(self, degrees):
        self._check_image_loaded()
        self.image = self.image.rotate(degrees)

    def adjust_brightness(self, factor):
        self._check_image_loaded()
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(factor)

    def _check_image_loaded(self):
        if self.image is None:
            raise ValueError("No image loaded. Please load an image first.")