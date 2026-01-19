def save_image(self, save_path):
    """
    यदि छवि खोली गई है तो छवि को एक पथ पर सहेजें
    :param save_path: str, वह पथ जहाँ छवि सहेजी जाएगी
    >>> processor.load_image('test.jpg')
    >>> processor.save_image('test2.jpg')
    """
    if self.image is not None:
        self.image.save(save_path)
    else:
        raise ValueError("No image loaded to save")