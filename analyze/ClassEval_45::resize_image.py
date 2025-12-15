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