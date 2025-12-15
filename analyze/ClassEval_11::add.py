class BitStatusUtil: 

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
            if arg < 0:
                raise ValueError(f"{arg} must be greater than or equal to 0")
            if arg % 2 != 0:
                raise ValueError(f"{arg} not even")

    @staticmethod
    def add(states, stat):
        """
        मौजूदा स्टेटस में एक स्टेटस जोड़ें, और पैरामीटर्स चेक करें कि वे लीगल हैं या नहीं।

        :param states: मौजूदा स्टेटस, int.
        :param stat: जोड़ा जाने वाला स्टेटस, int.
        :return: स्टेटस जोड़ने के बाद का स्टेटस, int.

        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.add(2, 4)
        6
        """
        BitStatusUtil.check([states, stat])
        return states | stat