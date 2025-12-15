class BitStatusUtil: 

    def add(states, stat):
        """
        Add a status to the current status,and check the parameters wheather they are legal.
        :param states: Current status,int.
        :param stat: Status to be added,int.
        :return: The status after adding the status,int.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.add(2,4)
        6
        """
        BitStatusUtil.check([states, stat])
        return states | stat
    
    @staticmethod
    def has(states, stat):
        """
            Check if the current status contains the specified status,and check the parameters wheather they are legal.
            :param states: Current status,int.
            :param stat: Specified status,int.
            :return: True if the current status contains the specified status,otherwise False,bool.
            >>> bit_status_util = BitStatusUtil()
            >>> bit_status_util.has(6,2)
            True
        """
        BitStatusUtil.check([states, stat])
        return (states & stat) == stat
    
    @staticmethod
    def remove(states, stat):
        """
            Remove the specified status from the current status,and check the parameters wheather they are legal.
            :param states: Current status,int.
            :param stat: Specified status,int.
            :return: The status after removing the specified status,int.
            >>> bit_status_util = BitStatusUtil()
            >>> bit_status_util.remove(6,2)
            4
        """
        BitStatusUtil.check([states, stat])
        if BitStatusUtil.has(states, stat):
            return states ^ stat
        return states

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
            if arg < 0 or arg % 2 != 0:
                raise ValueError(f"{arg} 不是偶数")