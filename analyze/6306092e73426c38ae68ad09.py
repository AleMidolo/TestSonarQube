def validate_length_args(self, args):
    """
    检查给定参数的值是否不超过指定的长度。

    :param args: 接收到的参数。

    检查参数的值是否不超过指定的长度。

    :param args: 接收到的参数。
    """
    # 遍历所有参数
    for arg_name, arg_value in args.items():
        # 如果参数值是字符串类型
        if isinstance(arg_value, str):
            # 获取该参数允许的最大长度
            max_length = self.get_max_length(arg_name)
            
            # 如果设置了最大长度限制
            if max_length is not None:
                # 检查参数值长度是否超过限制
                if len(arg_value) > max_length:
                    raise ValueError(f"Parameter '{arg_name}' exceeds maximum length of {max_length}")
                    
    return True