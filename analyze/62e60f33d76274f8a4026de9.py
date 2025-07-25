def dehydrate_point(value):
    """
    结构类是根据值的长度生成的。
    用于处理 Point 数据的转换器

    :param value: Point 对象
    :type value: Point
    :return: 转换后的结构
    :rtype: dict
    """
    if not value:
        return {}
    
    # 假设 Point 对象有 x 和 y 属性
    return {
        'x': value.x,
        'y': value.y
    }