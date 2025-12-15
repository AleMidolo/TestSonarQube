def rotate_image(self, degrees):
        """
        如果图像已打开，则旋转图像
        :param degrees: float，图像将旋转的角度
        >>> processor.load_image('test.jpg')
        >>> processor.rotate_image(90)
        >>> processor.image.size
        (4096, 3072)
        """
        
        if self.image:
            self.image = self.image.rotate(degrees, expand=True)