@staticmethod
def has(states, stat):
    """
    检查当前状态是否包含指定状态，并检查参数是否合法。
    :param states: 当前状态，int。
    :param stat: 指定状态，int。
    :return: 如果当前状态包含指定状态，则返回 True；否则返回 False，bool。
    >>> bit_status_util = BitStatusUtil()
    >>> bit_status_util.has(6,2)
    True

    """
    return (states & stat) == stat