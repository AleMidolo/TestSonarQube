def resize_image(self, width, height):
        """
        Ridimensiona l'immagine se l'immagine è stata aperta.
        :param width: int, la larghezza target dell'immagine
        :param height: int, l'altezza target dell'immagine
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(300, 300)
        >>> processor.image.width
        300
        >>> processor.image.height
        300
        """
        if self.image:
            self.image = self.image.resize((width, height))