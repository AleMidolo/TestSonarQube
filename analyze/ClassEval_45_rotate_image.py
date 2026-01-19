def rotate_image(self, degrees):
    """
        यदि छवि खोली गई है तो छवि को घुमाएँ
        :param degrees: float, वह डिग्री जिसमें छवि को घुमाया जाएगा
        >>> processor.load_image('test.jpg')
        >>> processor.rotate_image(90)
        >>> processor.image.size
        (4096, 3072)
        """
    if self.image:
        self.image = self.image.rotate(degrees, expand=True)