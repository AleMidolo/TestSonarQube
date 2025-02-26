def index(self, key):
    """
    以整数形式返回键。
    返回给定项的索引。

    :param key: 一个键
    :return: 索引
    :rtype: int
    """
    try:
        return self.items.index(key)
    except ValueError:
        return -1