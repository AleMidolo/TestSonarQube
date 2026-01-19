def add_argument(self, arg, required=False, arg_type=str):
    """
    将参数添加到 self.types 和 self.required。
    检查它是否是一个必需的参数并存储参数类型。
    如果参数被设置为必需,它将被添加到必需集合中。
    参数类型和名称作为键值对存储在 types 字典中。
    :param arg: str, 参数名称
    :param required: bool, 参数是否为必需,默认为 False
    :param arg_type: str, 参数类型,默认为字符串
    >>> parser.add_argument('arg1', True, 'int')
    >>> parser.required
    {'arg1'}
    >>> parser.types
    {'arg1': 'int'}
    """
    # 将参数类型存储到 types 字典中
    self.types[arg] = arg_type
    
    # 如果参数是必需的,将其添加到 required 集合中
    if required:
        self.required.add(arg)