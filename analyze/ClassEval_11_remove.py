@staticmethod
def remove(states, stat):
    """
    从当前状态中移除指定状态,并检查参数是否合法。
    :param states: 当前状态,int。
    :param stat: 指定状态,int。
    :return: 移除指定状态后的状态,int。
    >>> bit_status_util = BitStatusUtil()
    >>> bit_status_util.remove(6,2)
    4

    """
    return states & ~stat