def load_image(self, image_path):
    """
        PIL में इमेज उपयोग का उपयोग करके एक इमेज खोलें
        :param image_path: str, इमेज का पथ जो खोला जाना है
        >>> processor.load_image('test.jpg')
        >>> processor.image
        <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3072x4096 at 0x194F2412A48>
        """
    try:
        self.image = Image.open(image_path)
    except Exception as e:
        print(f'Error loading image: {e}')
        self.image = None