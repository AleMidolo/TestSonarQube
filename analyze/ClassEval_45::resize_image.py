def resize_image(self, width, height):
        """
        如果图像已打开，则调整图像大小。
        :param width: int, 图像的目标宽度
        :param height: int, 图像的目标高度
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(300, 300)
        >>> processor.image.width
        300
        >>> processor.image.height
        300
        """
        if self.image:
            self.image = self.image.resize((width, height))