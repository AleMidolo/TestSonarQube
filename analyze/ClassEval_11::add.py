@staticmethod
def add(states, stat):
    """
        将状态添加到当前状态，并检查参数是否合法。
        :param states: 当前状态，int。
        :param stat: 要添加的状态，int。
        :return: 添加状态后的状态，int。
        >>> bit_status_util = BitStatusUtil()
        >>> bit_status_util.add(2,4)
        6

        """
    BitStatusUtil.check([states, stat])
    if not BitStatusUtil.has(states, stat):
        return states | stat
    return states