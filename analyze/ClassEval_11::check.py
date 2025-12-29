@staticmethod
def check(args):
    """
        Check if the parameters are legal, args must be greater than or equal to 0 and must be even,if not,raise ValueError.
        :param args: Parameters to be checked,list.
        :return: None.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.check([2,3,4])
        Traceback (most recent call last):
        ...
        ValueError: 3 not even
        """
    for arg in args:
        if not isinstance(arg, int):
            raise ValueError(f'{arg} not int')
        if arg < 0:
            raise ValueError(f'{arg} less than 0')
        if arg % 2 != 0:
            raise ValueError(f'{arg} not even')