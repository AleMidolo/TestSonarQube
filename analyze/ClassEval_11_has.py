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
    if not isinstance(states, int) or not isinstance(stat, int):
        return False
    
    if states < 0 or stat < 0:
        return False
    
    return (states & stat) == stat