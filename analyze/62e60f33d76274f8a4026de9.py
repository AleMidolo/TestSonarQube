def dehydrate_point(value):
    """
    结构类是根据值的长度生成的。
    用于处理 Point 数据的转换器

    :param value: Point 对象
    :type value: Point
    :return: 转换后的数据结构
    :rtype: dict
    """
    if hasattr(value, 'x') and hasattr(value, 'y'):
        return {'x': value.x, 'y': value.y}
    else:
        raise ValueError("Invalid Point object: missing 'x' or 'y' attribute")