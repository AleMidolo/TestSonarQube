def dehydrate_point(value):
    """
    结构类是根据值的长度生成的。
    用于处理 Point 数据的转换器

    :param value: Point 对象
    :type value: Point
    :return: 转换后的结构类
    :rtype: dict
    """
    if not hasattr(value, 'x') or not hasattr(value, 'y'):
        raise ValueError("The input value must be a Point object with 'x' and 'y' attributes.")
    
    return {
        'x': value.x,
        'y': value.y
    }