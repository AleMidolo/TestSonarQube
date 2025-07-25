def index(self, key):
    """
    以整数形式返回键。
    返回给定项的索引。

    :param key: 一个键
    :return: 索引
    :rtype: int
    """
    if key in self:
        return self.keys().index(key)
    else:
        raise KeyError(f"Key {key} not found.")