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
    if not isinstance(states, int) or not isinstance(stat, int):
        raise TypeError("Both states and stat must be integers")
    
    if states < 0 or stat < 0:
        raise ValueError("Both states and stat must be non-negative integers")
    
    return states | stat