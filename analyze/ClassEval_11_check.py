@staticmethod
def check(args):
    """
        检查参数是否合法，args 必须大于或等于 0 且必须是偶数，如果不是，则引发 ValueError。
        :param args: 要检查的参数，列表。
        :return: None。
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.check([2,3,4])
        Traceback (most recent call last):
        ...
        ValueError: 3 不是偶数
        """
    for arg in args:
        if not isinstance(arg, int):
            raise ValueError(f'{arg} 不是整数')
        if arg < 0:
            raise ValueError(f'{arg} 小于 0')
        if arg % 2 != 0:
            raise ValueError(f'{arg} 不是偶数')