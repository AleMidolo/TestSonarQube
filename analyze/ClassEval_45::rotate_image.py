def rotate_image(self, degrees):
    """
        यदि छवि खोली गई है तो छवि को घुमाएँ
        :param degrees: float, वह डिग्री जिसमें छवि को घुमाया जाएगा
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(90)
        """
    if self.image:
        self.image = self.image.rotate(degrees, expand=True)