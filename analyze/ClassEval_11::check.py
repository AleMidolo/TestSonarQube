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
        Controlla se i parametri sono legali, args deve essere maggiore o uguale a 0 e deve essere pari, altrimenti solleva ValueError.
        :param args: Parametri da controllare, lista.
        :return: Nessuno.
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.check([2,3,4])
        Traceback (most recent call last):
        ...
        ValueError: 3 non è pari
        """
        for arg in args:
            if arg < 0:
                raise ValueError(f"{arg} non è maggiore o uguale a 0")
            if arg % 2 != 0:
                raise ValueError(f"{arg} non è pari")