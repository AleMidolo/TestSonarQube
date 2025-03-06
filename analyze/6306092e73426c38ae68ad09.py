def validate_length_args(self, args):
    """
    检查给定参数的值是否不超过指定的长度。

    :param args: 接收到的参数。
    :return: 如果所有参数的长度都符合要求，返回True；否则返回False。
    """
    max_length = 100  # 假设最大长度为100
    for arg in args:
        if len(str(arg)) > max_length:
            return False
    return True