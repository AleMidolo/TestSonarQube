def validate_length_args(self, args):
    """
    检查给定参数的值是否不超过指定的长度。

    :param args: 接收到的参数。
    """
    max_length = 100  # 假设最大长度为100
    for key, value in args.items():
        if isinstance(value, str) and len(value) > max_length:
            raise ValueError(f"参数 '{key}' 的长度超过了最大允许长度 {max_length}")
        elif isinstance(value, (list, tuple)) and len(value) > max_length:
            raise ValueError(f"参数 '{key}' 的长度超过了最大允许长度 {max_length}")
    return True