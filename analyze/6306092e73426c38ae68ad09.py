def validate_length_args(self, args):
    """
    检查给定参数的值是否不超过指定的长度。

    :param args: 接收到的参数。

    检查参数的值是否不超过指定的长度。

    :param args: 接收到的参数。
    """
    # 定义最大长度限制
    MAX_LENGTH = 255

    # 遍历所有参数
    for key, value in args.items():
        # 如果值是字符串类型
        if isinstance(value, str):
            # 检查长度是否超过限制
            if len(value) > MAX_LENGTH:
                raise ValueError(f"Parameter '{key}' exceeds maximum length of {MAX_LENGTH} characters")
            
        # 如果值是列表、元组或集合类型
        elif isinstance(value, (list, tuple, set)):
            if len(value) > MAX_LENGTH:
                raise ValueError(f"Parameter '{key}' exceeds maximum length of {MAX_LENGTH} items")
            
        # 如果值是字典类型
        elif isinstance(value, dict):
            if len(value) > MAX_LENGTH:
                raise ValueError(f"Parameter '{key}' exceeds maximum length of {MAX_LENGTH} key-value pairs")

    return True