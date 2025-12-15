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
    def has(states, stat):
        """
        Controlla se lo stato attuale contiene lo stato specificato e verifica se i parametri sono legali.
        :param states: Stato attuale, int.
        :param stat: Stato specificato, int.
        :return: True se lo stato attuale contiene lo stato specificato, altrimenti False, bool.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.has(6,2)
        True

        """
        BitStatusUtil.check([states, stat])
        return (states & stat) == stat