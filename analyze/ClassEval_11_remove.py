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
    if not isinstance(states, int) or not isinstance(stat, int):
        raise TypeError("Both states and stat must be integers")
    
    if states < 0 or stat < 0:
        raise ValueError("Both states and stat must be non-negative")
    
    # Remove the specified status by using bitwise AND with the complement of stat
    return states & ~stat